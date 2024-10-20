import unittest
from is_odd_ai import OddChecker

class TestOddChecker(unittest.TestCase):
    def setUp(self):
        self.api_key = ""
        self.is_odd_checker = OddChecker(api_key=self.api_key)

    def test_is_odd(self):
        self.assertEqual(self.is_odd_checker.is_odd(5), True)

    def test_is_even(self):
        self.assertEqual(self.is_odd_checker.is_odd(6), False)
    
    def test_is_odd_with_negative_number(self):
        self.assertEqual(self.is_odd_checker.is_odd(-2883), True)

    def test_is_even_with_negative_number(self):
        self.assertEqual(self.is_odd_checker.is_odd(-2814), False)

    def test_zero_is_odd(self):
        self.assertEqual(self.is_odd_checker.is_odd(0), False)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.is_odd_checker.is_odd("abc")

if __name__ == '__main__':
    unittest.main()