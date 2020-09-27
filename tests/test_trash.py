import unittest

import trash.trash as trash


class TestCase(unittest.TestCase):
    def test_get_next_trash_day_monday(self):
        today = '2020-09-28'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_tuesday(self):
        today = '2020-09-22'
        expected_next_trash_day = '2020-09-22'
        next_trash_day = trash.next_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_wednesday(self):
        today = '2020-09-23'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_thursday(self):
        today = '2020-09-24'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_friday(self):
        today = '2020-09-25'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_saturday(self):
        today = '2020-09-26'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)

    def test_get_trash_day_sunday(self):
        today = '2020-09-27'
        expected_next_trash_day = '2020-09-29'
        next_trash_day = trash.next_trash_day(today)
        self.assertEqual(expected_next_trash_day, next_trash_day)


if __name__ == '__main__':
    unittest.main()
