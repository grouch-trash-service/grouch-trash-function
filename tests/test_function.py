import unittest
from trash import function


class Test(unittest.TestCase):
    def test_default_lambda_handler(self):
        event = {'date': '2020-09-09'}
        result = function.lambda_handler(event, None)
        self.assertEqual({'default': 'Tuesday'}, result)

    def test_holiday_lambda_handler(self):
        event = {'date': '2020-01-01'}
        result = function.lambda_handler(event, None)
        self.assertEqual({'holiday': "New Year's Day"}, result)


if __name__ == '__main__':
    unittest.main()
