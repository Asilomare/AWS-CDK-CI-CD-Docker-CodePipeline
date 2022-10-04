from aws_cdk as core
from pipeline.lambda_stack import LambdaStack

def test_lambda_handler():

    # GIVEN
    app = core.App()

    # WHEN
    LambdaStack(app, 'lambdastage', 'UnitTestTag')

    # THEN
    template = app.synth().get_stack_by_name('lambdastage').template
    functions = [resource for resource in template['Resources'].values()
                if resource['Type'] == 'AWS::Lambda::Function']

    assert len(functions) == 1
    assert functions[0]['Properties']['PackageType'] == 'Image'
    assert functions[0]['Properties']['Timeout'] == 150