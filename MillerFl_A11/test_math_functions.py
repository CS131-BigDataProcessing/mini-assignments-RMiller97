# test_math_functions.py
import unittest
from math_functions import divide, power

class TestMathFunctions(unittest.TestCase):
    # Test for divide function
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_divide_by_negative(self):
        self.assertEqual(divide(6, -3), -2)

    def test_divide_result_double(self):
        self.assertEqual(divide(5, 2), 2.5)

    # Test for power function
    def test_power_undefined(self):
        with self.assertRaises(ValueError):
            power(0, -1)

    def test_power_zero_exp(self):
        self.assertEqual(power(3, 0), 1)

    def test_power_negative_exp(self):
        self.assertEqual(power(4, -1), 0.25)

if __name__ == '__main__':
    unittest.main()
