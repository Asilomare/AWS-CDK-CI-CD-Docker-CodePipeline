import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

from pipeline.lambda_stack import LambdaStack

class LambdaStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        LambdaStack(self, "LambdaStack")
    
    
class PipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source = CodePipelineSource.git_hub("Asilomare/WebScraper", "master")
        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="Pipeline",
                        synth=ShellStep("Synth", 
                            input=source,
                            commands=["python -m pip install -r lambda-requirements.txt -t lambda",
                                "python -m pip install -r requirements.txt",
                                "npx cdk synth"]
                        )
                    )
        pipeline.add_stage(LambdaStage(self, 'lambdastage'))