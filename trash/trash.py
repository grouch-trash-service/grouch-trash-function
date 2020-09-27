"""
Module for calculating next trash day
"""
import datetime
from dateutil import parser

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
