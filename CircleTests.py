import unittest
import circle
import math


class CircleTests(unittest.TestCase):

    def test_area_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(0.0, res)

    def test_area_five_mul(self):
        res = circle.area(5)
        self.assertEqual(math.pi * (5 ** 2), res)

    def test_area_eleven_mul(self):
        res = circle.area(11)
        self.assertEqual(math.pi * (11 ** 2), res)

    def test_length_zero_mul(self):
        res = circle.length(0)
        self.assertEqual(0.0, res)

    def test_length_five_mul(self):
        res = circle.length(5)
        self.assertEqual(math.pi * 2 * 5, res)

    def test_length_eleven_mul(self):
        res = circle.length(11)
        self.assertEqual(math.pi * 2 * 11, res)
