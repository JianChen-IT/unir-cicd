import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(
            4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(
            0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(
            0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0,
                               util.convert_to_number("-1.0"), delta=0.0000001)

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())

    def test_inputs_with_two_valid_number(self):
        try:
            util.check_types(1, 2)
        except TypeError:
            assert False

    def test_inputs_with_two_number_with_decimals(self):
        try:
            util.check_types(1.0, 2.0)
        except TypeError:
            assert False

    def test_inputs_with_two_number_one_invalid(self):
        self.assertRaises(TypeError, util.check_types, "1", "$")
        self.assertRaises(TypeError, util.check_types, "abcd", "5")

    def test_inputs_with_one_valid_number(self):
        try:
            util.check_types(5)
        except TypeError:
            assert False

    def test_inputs_with_one_valid_number_with_decimals(self):
        try:
            util.check_types(5.17)
        except TypeError:
            assert False

    def test_inputs_with_one_not_valid_inpunt(self):
        self.assertRaises(TypeError, util.check_types, "UN1R")
        self.assertRaises(TypeError, util.check_types, "213$431@")
