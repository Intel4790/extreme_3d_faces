import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def test_sample_util_function(self):
        result = utils.sample_util_function()
        self.assertEqual(result, "Expected Result")

if __name__ == '__main__':
    unittest.main()