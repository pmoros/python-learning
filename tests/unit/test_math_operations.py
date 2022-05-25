import unittest
from app.math_operations import Calculator


class TestCalculator(unittest.TestCase):
    def test_should_add_two_numbers(self):
        a = 1
        b = 4

        result = Calculator.add(a, b)
        self.assertEqual(result, 5)
