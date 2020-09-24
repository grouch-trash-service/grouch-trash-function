"""
Module for Holiday operations
"""
import datetime

import holidays

us_holidays = holidays.UnitedStates()


def contains_holiday(dates: list) -> bool:
    """
    determines if a date range contains a holiday
    :param dates: list of dates
    :return: True if the list contains a holiday, else False
    """

    for date in dates:
        if date in us_holidays:
            return True
    return False

def get_holiday(dates: list) -> bool:
    """
    gets the first holiday in a list of dates
    :param dates: list of dates containing potential holidays
    :return: the first holiday in the list. None if there are no holidays.
    """
    for date in dates:
        if date in us_holidays:
            return us_holidays.get(date)
    return None

def create_date_range(start_date: datetime.date, number_of_days: int) -> list:
    """
    creates a date range from a start date and number of days
    :param start_date: day to start the range
    :param number_of_days: number of days that should be in the range
    :return: a list containing all the days in the date range
    """
    return [start_date + datetime.timedelta(days=day) for day in range(number_of_days)]
