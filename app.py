import aws_cdk as cdk
from constructs import Construct
from pipeline.pipeline_stack import PipelineStack

app = cdk.App()
PipelineStack(app, "PipelineStack")

app.synth()
