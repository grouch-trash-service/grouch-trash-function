import json
import boto3
import botocore

from behave import use_step_matcher, given, when, then

use_step_matcher("re")


@given("a date with no holidays during the week")
def given_no_holiday(context):
    context.date = '2020-09-22'


@given("a (?P<date>.+) with a holiday during the week")
def holiday_during_the_week(context, date):
    """
    :type context: behave.runner.Context
    :type date: str
    """
    context.date = date


@when("getting the trash day for that week")
def get_trash_day(context):
    env = context.config.userdata.get('local', 'false')
    if env == 'true':
        lambda_client = boto3.client('lambda',
                                     region_name='us-east-1',
                                     endpoint_url='http://127.0.0.1:3001',
                                     use_ssl=False,
                                     verify=False,
                                     config=botocore.client.Config(
                                         signature_version=botocore.UNSIGNED,
                                         read_timeout=600,
                                         retries={'max_attempts': 0}
                                     )
                                     )
    else:
        lambda_client = boto3.client('lambda')
    event = {
        'date': context.date
    }
    payload = json.dumps(event).encode('utf-8')
    context.response = lambda_client.invoke(FunctionName='TrashFunction', Payload=payload)


@then("the default trash day is returned")
def default_is_returned(context):
    payload = context.response['Payload']
    response_body = json.loads(payload._raw_stream.data)
    assert response_body == {'type': 'default', 'schedule': 'Tuesday'}


@then("the (?P<holiday>.+) trash schedule is returned")
def step_impl(context, holiday):
    """
    :type context: behave.runner.Context
    :type holiday: str
    """
    payload = context.response['Payload']
    response_body = json.loads(payload._raw_stream.data)
    assert response_body['holiday'] == holiday
