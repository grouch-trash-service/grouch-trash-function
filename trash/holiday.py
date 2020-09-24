"""
Module for Holiday operations
"""
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
