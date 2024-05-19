import square
import unittest


class SquareTests(unittest.TestCase):

    def test_area_zero_mul(self):
        res = square.area(0)
        self.assertEqual(0, res)

    def test_area_ten_mul(self):
        res = square.area(10)
        self.assertEqual(10 * 10, res)

    def test_area_twelve_mul(self):
        res = square.area(12)
        self.assertEqual(12 * 12, res)

    def test_perimeter_zero_mul(self):
        res = square.perimeter(0)
        self.assertEqual(0, res)

    def test_perimeter_eleven_mul(self):
        res = square.perimeter(11)
        self.assertEqual(11 * 4, res)

    def test_perimeter_thousand_mul(self):
        res = square.perimeter(1000)
        self.assertEqual(1000 * 4, res)
