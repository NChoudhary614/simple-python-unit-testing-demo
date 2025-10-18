import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from src.main import my_function

class TestMyFunction(unittest.TestCase):
    def test_positive_numbers(self):
        result = my_function(1, 2)
        self.assertEqual(result, 3)

    def test_negative_numbers(self):
        result = my_function(-1, -2)
        self.assertEqual(result, -3)

if __name__ == '__main__':
    unittest.main()
