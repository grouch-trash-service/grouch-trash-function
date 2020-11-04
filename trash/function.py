"""
lambda function for getting which day of the week trash pickup is
"""
import os
import logging
import logging.config
import configparser
import trash_day as trash
from schedule import TrashScheduleService

config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_file)
trash_schedule_service = TrashScheduleService(config['DEFAULT']['TrashScheduleServiceUrl'])

logging.config.fileConfig(config_file)


def lambda_handler(event, context) -> dict:
    """
    lambda function handler for getting trash day
    :param event: lambda event
    :param context: lamdba context
    :return: dict containing trash day information
    """
    logging.info('Starting function with context=%s and event=%s', context, event)
    date = event['date']

    holiday_schedule = trash_schedule_service.get_schedule()
    trash_day = trash.next_trash_day(date, holiday_schedule)
    logging.info('Completed function with response=%s', trash_day)
    return trash_day
