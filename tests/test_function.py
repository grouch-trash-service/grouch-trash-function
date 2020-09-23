import unittest
from trash import function


class Test(unittest.TestCase):
    def test_lambda_handler(self):
        result = function.lambda_handler(None, None)
        self.assertEqual({'default': 'Tuesday'}, result)


if __name__ == '__main__':
    unittest.main()
