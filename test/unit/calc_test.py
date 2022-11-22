import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_power_method_return_correct_result(self):
        self.assertEqual(4, self.calc.power(4, 1))
        self.assertEqual(64, self.calc.power(8, 2))
        self.assertEqual(243, self.calc.power(3, 5))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "4", "3")
        self.assertRaises(TypeError, self.calc.power, "$", 4)
        self.assertRaises(TypeError, self.calc.power, "UNIR", 16)

    def test_sqrt_method_return_correct_result(self):
        self.assertEqual(4, self.calc.sqrt(16))
        self.assertEqual(252, self.calc.sqrt(63504))

    def test_sqrt_method_fails_with_not_valid_number(self):
        self.assertRaises(ValueError, self.calc.sqrt, -1)
        self.assertRaises(ValueError, self.calc.sqrt, -0.1)
        self.assertRaises(ValueError, self.calc.sqrt, -100)

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "4")
        self.assertRaises(TypeError, self.calc.sqrt, "$")
        self.assertRaises(TypeError, self.calc.sqrt, "UNIR")

    def test_log_method_return_correct_result(self):
        self.assertAlmostEqual(1, self.calc.log(10), delta=0.00001)
        self.assertAlmostEqual(2, self.calc.log(100), delta=0.00001)
        self.assertAlmostEqual(3, self.calc.log(1000), delta=0.00001)

    def test_log_method_fails_with_not_valid_number(self):
        self.assertRaises(ValueError, self.calc.log, 0)
        self.assertRaises(ValueError, self.calc.log, -10)

    def test_log_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log, "10")
        self.assertRaises(TypeError, self.calc.log, "$")
        self.assertRaises(TypeError, self.calc.log, "UNIR")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
