import unittest
from divider import divide, average

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

if __name__ == '__main__':
    unittest.main()
