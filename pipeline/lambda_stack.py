from aws_cdk import (
    aws_lambda as _lambda,
    aws_events as events,
    aws_iam as iam,
    aws_s3 as s3,
    aws_events_targets as targets,
    App, Stack, Duration
)

class LambdaStack(Stack):
    def __init__(self, app: App, id: str) -> None:
        super().__init__(app, id)

        bucket = s3.Bucket(self, "WebScraperDumpBucket")
        
        
        #lambda from docker image
        function = _lambda.DockerImageFunction(self, "lambda_function_docker",
            code=_lambda.DockerImageCode.from_image_asset(
                directory="lambda/"),
            timeout=Duration.seconds(150),
            environment={ 
                 "bucket": bucket.bucket_name,
            }
        )
    
        bucket.grant_put(function)
        
        #eventbridge daily trigger
        rule = events.Rule(self, "Run Daily",
            schedule=events.Schedule.cron(minute="0", hour="5", week_day="*", month="*", year="*")
        )
        rule.add_target(targets.LambdaFunction(function))
        
        
