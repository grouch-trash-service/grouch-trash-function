import unittest
import datetime
import holiday


class TestCase(unittest.TestCase):
    def test_holiday_in_range(self):
        number_of_days = 7
        start_date = datetime.date(2019, 12, 31)
        date_range = self.__create_date_range(start_date, number_of_days)
        self.assertTrue(holiday.contains_holiday(date_range))

    def test_holiday_not_in_range(self):
        number_of_days = 7
        start_date = datetime.date(2019, 12, 1)
        date_range = self.__create_date_range(start_date, number_of_days)
        self.assertFalse(holiday.contains_holiday(date_range))

    def __create_date_range(self, start_date, number_of_days):
        return [start_date + datetime.timedelta(days=day) for day in range(number_of_days)]


if __name__ == '__main__':
    unittest.main()
