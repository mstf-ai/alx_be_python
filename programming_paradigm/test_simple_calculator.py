import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Initialize a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- Addition Tests ----------
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -5), -6)
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)

    # ---------- Subtraction Tests ----------
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 10), 10)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(-3, 4), -7)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7, 0), 7)

    # ---------- Multiplication Tests ----------
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # ---------- Division Tests ----------
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(20, 5), 4)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-20, -4), 5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_result_decimal(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

if __name__ == "__main__":
    unittest.main()
