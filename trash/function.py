"""
lambda function for getting which day of the week trash pickup is
"""

from dateutil import parser

import holiday


def lambda_handler(event, context) -> dict:
    """
    lambda function handler for getting trash day
    :param event: lambda event
    :param context: lamdba context
    :return: dict containing trash day information
    """
    print(event)
    print(context)
    day_range = 7
    start_date = parser.parse(event['date'])
    date_range = holiday.create_date_range(start_date, day_range)

    if holiday.contains_holiday(date_range):
        response = {'holiday': holiday.get_holiday(date_range)}
    else:
        response = {'default': 'Tuesday'}
    print(response)

    return response
