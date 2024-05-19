import unittest
import rectangle


class RectangleTests(unittest.TestCase):

    def test_area_zero_mul(self):
        res = rectangle.area(0, 0)
        self.assertEqual(0, res)

    def test_area_ten_one_mul(self):
        res = rectangle.area(10, 1)
        self.assertEqual(10 * 1, res)

    def test_area_thousand_three_mul(self):
        res = rectangle.area(1000, 3)
        self.assertEqual(1000 * 3, res)

    def test_perimeter_zero_add(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(0, res)

    def test_perimeter_two_five_add(self):
        res = rectangle.perimeter(2, 5)
        self.assertEqual((2 + 5) * 2, res)

    def test_perimeter_ten_eleven_add(self):
        res = rectangle.perimeter(10, 11)
        self.assertEqual((10 + 11) * 2, res)
