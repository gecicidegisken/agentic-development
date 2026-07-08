import unittest
from divider import divide, average, add, subtract, multiply

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

    def test_add_success(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)

    def test_subtract_success(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(2.5, 1.0), 1.5)

    def test_multiply_success(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(1.5, 2), 3.0)

if __name__ == '__main__':
    unittest.main()
