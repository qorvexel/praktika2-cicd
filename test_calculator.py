import unittest

from calculator import add, multiply


class TestCalculator(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_zero(self):
        self.assertEqual(multiply(5, 0), 0)


if __name__ == "__main__":
    unittest.main()
