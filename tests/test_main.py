import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def test_main_function(self):
        self.assertEqual(main.main_function(), "Expected Result")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()