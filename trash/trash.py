"""
Module for calculating next trash day
"""
import datetime
from dateutil import parser

import holiday

TUESDAY = 1
TRASH_DAY = TUESDAY


def next_trash_day(date: str) -> str:
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
