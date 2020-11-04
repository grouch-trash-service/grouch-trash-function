"""
Module for calculating next trash day
"""
import datetime
import calendar
import configparser
import os

from dateutil import parser

import holiday


config = configparser.ConfigParser()
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_file)

TRASH_DAY = int(config['DEFAULT']['TrashDay'])


def next_regular_trash_day(date: str) -> str:
    """
    Gets the next trash day for a given date
    :param date: data to calculate trash day for
    :return: date of next trash pickup
    """
    parsed_date = parser.parse(date)
    day_of_week = parsed_date.weekday()

    if day_of_week < TRASH_DAY:
        delta = TRASH_DAY - day_of_week
    elif day_of_week == TRASH_DAY:
        delta = 0
    else:
        delta = 7 - (day_of_week - TRASH_DAY)

    next_trash_date = parsed_date + datetime.timedelta(days=delta)
    return next_trash_date.strftime('%Y-%m-%d')


def get_weekdays(date: str) -> list:
    """
    get a list containing each day in the week for a specific date
    :param date: date to get the weekdays for
    :return: list with all dates starting with Monday ending in Sunday
    """
    parsed_date = parser.parse(date)
    day_of_week = parsed_date.weekday()
    first_day_of_week = parsed_date - datetime.timedelta(days=day_of_week)

    return holiday.create_date_range(first_day_of_week, 7)


def next_trash_day(date: str, holidays: list) -> dict:
    """
    gets the next trash day taking holidays into consideration
    :param date: date to calculate next trash day for
    :param holidays: list of holidays
    :return: dict containing either the default trash day or route delay information based off holiday.
    """
    next_regular = next_regular_trash_day(date)
    weekdays = get_weekdays(next_regular)
    if holiday.contains_holiday(weekdays):
        holiday_name = holiday.get_holiday(weekdays)
        delay = list(filter(lambda holiday_delays: holiday_delays['name'] == holiday_name, holidays))[0]['routeDelays']
        trash_day = {'type': 'holiday', 'holiday': holiday_name, 'schedule': delay}
    else:
        trash_day = {'type': 'default', 'schedule': calendar.day_name[TRASH_DAY]}

    return trash_day
