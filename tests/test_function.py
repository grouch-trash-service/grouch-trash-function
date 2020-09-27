import unittest
from unittest.mock import MagicMock

from schedule import TrashScheduleService
from trash import function


class Test(unittest.TestCase):
    holidays = [{
        'name': 'Christmas Day',
        'routeDelays': 'Delays!!'
    }]

    def test_lambda_handler(self):
        trash_schedule_service = TrashScheduleService(
            '/v1/holidays')
        trash_schedule_service.get_schedule = MagicMock(return_value=Test.holidays)

        function.trash_schedule_service = trash_schedule_service

        event = {'date': '2020-12-21'}
        result = function.lambda_handler(event, None)
        self.assertEqual({'holiday': 'Christmas Day', 'delay': 'Delays!!'}, result)


if __name__ == '__main__':
    unittest.main()
