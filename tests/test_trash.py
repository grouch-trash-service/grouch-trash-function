from dateutil import parser

import unittest
import holiday
import trash.trash as trash


class TestCase(unittest.TestCase):
    holidays = [{
        'name': 'Christmas Day',
        'routeDelays': 'All Routes delayed by one day'
    }]

    def test_get_next_trash_day_monday(self):
        today = '2020-09-28'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_regular_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_tuesday(self):
        today = '2020-09-22'
        expected_next_trash_day = '2020-09-22'
        next_trash_day = trash.next_regular_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_wednesday(self):
        today = '2020-09-23'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_regular_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_thursday(self):
        today = '2020-09-24'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_regular_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_friday(self):
        today = '2020-09-25'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_regular_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_saturday(self):
        today = '2020-09-26'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_regular_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_sunday(self):
        today = '2020-09-27'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_regular_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_days_of_week_monday(self):
        day = '2020-09-28'
        expected_dates = holiday.create_date_range(parser.parse(day), 7)
        days_of_week = trash.get_weekdays(day)
        self.assertEqual(expected_dates, days_of_week)

    def test_get_days_of_week_tuesday(self):
        day = '2020-09-29'
        expected_dates = holiday.create_date_range(parser.parse('2020-09-28'), 7)
        days_of_week = trash.get_weekdays(day)
        self.assertEqual(expected_dates, days_of_week)

    def test_get_days_of_week_wednesday(self):
        day = '2020-09-30'
        expected_dates = holiday.create_date_range(parser.parse('2020-09-28'), 7)
        days_of_week = trash.get_weekdays(day)
        self.assertEqual(expected_dates, days_of_week)

    def test_get_days_of_week_thursday(self):
        day = '2020-10-01'
        expected_dates = holiday.create_date_range(parser.parse('2020-09-28'), 7)
        days_of_week = trash.get_weekdays(day)
        self.assertEqual(expected_dates, days_of_week)

    def test_get_days_of_week_friday(self):
        day = '2020-10-02'
        expected_dates = holiday.create_date_range(parser.parse('2020-09-28'), 7)
        days_of_week = trash.get_weekdays(day)
        self.assertEqual(expected_dates, days_of_week)

    def test_get_days_of_week_saturday(self):
        day = '2020-10-03'
        expected_dates = holiday.create_date_range(parser.parse('2020-09-28'), 7)
        days_of_week = trash.get_weekdays(day)
        self.assertEqual(expected_dates, days_of_week)

    def test_get_days_of_week_sunday(self):
        day = '2020-10-04'
        expected_dates = holiday.create_date_range(parser.parse('2020-09-28'), 7)
        days_of_week = trash.get_weekdays(day)
        self.assertEqual(expected_dates, days_of_week)

    def test_get_trash_day_no_holiday(self):
        day = '2020-10-04'
        expected_day = {'default': 'Tuesday'}
        trash_day = trash.next_trash_day(day, TestCase.holidays)
        self.assertEqual(expected_day,trash_day)

    def test_get_trash_day_holiday(self):
        day = '2020-12-21'
        expected_day = {'holiday': 'Christmas Day', 'delay': TestCase.holidays[0]['routeDelays']}
        trash_day = trash.next_trash_day(day, TestCase.holidays)
        self.assertEqual(expected_day,trash_day)


if __name__ == '__main__':
    unittest.main()
