import unittest
from app.math_operations import Calculator


class TestCalculator(unittest.TestCase):
    def test_should_add_two_numbers(self):
        left_number = 1
        right_number = 4

        result = Calculator.add(left_number, right_number)
        self.assertEqual(result, 5)
