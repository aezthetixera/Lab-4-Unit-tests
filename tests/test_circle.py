import math
import unittest

from circle import circle_area, circle_perimeter


class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(1), math.pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(10), 100 * math.pi)

    def test_perimeter(self):
        self.assertEqual(circle_perimeter(1), 2 * math.pi)
        self.assertEqual(circle_perimeter(10), 20 * math.pi)
        self.assertEqual(circle_perimeter(0), 0)



