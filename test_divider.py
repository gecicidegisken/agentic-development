import unittest
from divider import divide, average, multiply, subtract

class TestDivider(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(9, 3), 3.0)
        self.assertEqual(divide(-10, 2), -5.0)

    def test_divide_by_zero(self):
        self.assertIsNone(divide(100, 0))
        self.assertIsNone(divide(0, 0))
        self.assertIsNone(divide(5, 0.0))

    def test_average_success(self):
        self.assertEqual(average([10, 20, 30]), 20.0)
        self.assertEqual(average([5]), 5.0)
        self.assertEqual(average([1.5, 2.5, 3.5, 4.5]), 3.0)

    def test_average_empty(self):
        self.assertIsNone(average([]))

    def test_multiply_success(self):
        # integers
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        # floats
        self.assertAlmostEqual(multiply(1.5, 2), 3.0)
        self.assertAlmostEqual(multiply(2.5, 0.4), 1.0)
        # type error handling
        self.assertIsNone(multiply(3, 'a'))

    def test_subtract_success(self):
        # integers
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(-2, -3), 1)
        # floats
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)
        # type error handling
        self.assertIsNone(subtract('a', 1))

if __name__ == '__main__':
    unittest.main()
