"""
lambda function for getting which day of the week trash pickup is
"""


def lambda_handler(event, context) -> dict:
    """
    lambda function handler for getting trash day
    :param event: lambda event
    :param context: lamdba context
    :return: dict containing trash day information
    """
    print(event)
    print(context)
    return {
        'default': 'Tuesday'
    }
