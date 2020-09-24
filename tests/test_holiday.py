import unittest
import datetime
import trash.holiday as holiday


class TestCase(unittest.TestCase):
    def test_holiday_in_range(self):
        number_of_days = 7
        start_date = datetime.date(2019, 12, 31)
        date_range = holiday.create_date_range(start_date, number_of_days)
        self.assertTrue(holiday.contains_holiday(date_range))

    def test_holiday_not_in_range(self):
        number_of_days = 7
        start_date = datetime.date(2019, 12, 1)
        date_range = holiday.create_date_range(start_date, number_of_days)
        self.assertFalse(holiday.contains_holiday(date_range))

    def test_create_date_range(self):
        start_date = datetime.date(2019, 12, 1)
        expected_date_range = [start_date, datetime.date(2019, 12, 2)]

        date_range = holiday.create_date_range(start_date, 2)
        self.assertEqual(expected_date_range, date_range)

    def test_get_holiday(self):
        number_of_days = 7
        start_date = datetime.date(2019, 12, 31)
        date_range = holiday.create_date_range(start_date, number_of_days)
        new_years_day = holiday.get_holiday(date_range)
        self.assertEqual("New Year's Day", new_years_day)

if __name__ == '__main__':
    unittest.main()
