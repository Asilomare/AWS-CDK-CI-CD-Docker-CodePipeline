from aws_cdk import (App, Stack)
from lambda_stack import LambdaLayerStack

app = App()
LambdaLayerStack(app, "lambda-cdk")
app.synth()
