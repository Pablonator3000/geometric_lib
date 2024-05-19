import triangle
import unittest


class TriangleTests(unittest.TestCase):

    def test_area_zero_mul(self):
        res = triangle.area(0, 0)
        self.assertEqual(0 * 0 / 2, res)

    def test_area_ten_five_mul(self):
        res = triangle.area(10, 5)
        self.assertEqual(10 * 5 / 2, res)

    def test_area_eleven_thousand_mul(self):
        res = triangle.area(11, 1000)
        self.assertEqual(11 * 1000 / 2, res)

    def test_perimetr_zero_add(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(0, res)

    def test_perimetr_two_five_three_add(self):
        res = triangle.perimeter(2, 3, 5)
        self.assertEqual(2 + 3 + 5, res)

    def test_perimetr_one_ten_eleven_add(self):
        res = triangle.perimeter(1, 10, 11)
        self.assertEqual(1 + 10 + 11, res)
