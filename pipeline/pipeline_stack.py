import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
import aws_cdk.aws_codepipeline_actions as codepipeline_actions
from pipeline.lambda_stack import LambdaStack
from aws_cdk.aws_lambda import Function

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
                            commands=[
                                "python -m pip install -r requirements.txt",
                                "npx cdk synth"
                                ]
                        )
                    )
        #lambda test 
        function = Function.from_function_name(self,
            "lambda_function_docker", "lambda_function_docker"
        )
        codepipeline_actions.LambdaInvokeAction(
            action_name = "invoke_Lambda_Action",
            lambda_ = function
        ) 
        #lambda stage           
        pipeline.add_stage(LambdaStage(self, 'lambdastage'))
