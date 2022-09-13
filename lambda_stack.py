from aws_cdk import (
    aws_lambda as _lambda,
    aws_events as events,
    aws_iam as iam,
    aws_s3 as s3,
    aws_events_targets as targets,
    App, Stack, Duration
)
#make portable s3 bucket
#put_object permissions

#dependancys!!
#pip install -r lambda-requirements.txt -t lambda

# https://docs.aws.amazon.com/cdk/api/v1/python/modules.html
class LambdaLayerStack(Stack):
    def __init__(self, app: App, id: str) -> None:
        super().__init__(app, id)
        
        #inlined lambda function (see lambda_function.py)
        function = _lambda.Function(self, "lambda_function",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambda"),
            timeout=Duration.seconds(150)
        )
    
        #eventbridge daily trigger
        rule = events.Rule(self, "Run Daily",
            schedule=events.Schedule.cron(minute="0", hour="5", week_day="*", month="*", year="*")
        )
        rule.add_target(targets.LambdaFunction(function))
        
        bucket = s3.Bucket.from_bucket_name(self, "existingBucket", "webscraperbucket123123")
        bucket.grant_put(function)

