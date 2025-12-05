import unittest

from triangle import triangle_area, triangle_perimeter


class TestTriangle(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(triangle_area(10, 10), 50.0)
        self.assertEqual(triangle_area(1, 10), 5.0)
        self.assertEqual(triangle_area(6, 8), 24.0)

    def test_area_zero(self):
        self.assertEqual(triangle_area(0, 10), 0.0)
        self.assertEqual(triangle_area(10, 0), 0.0)

    def test_perimeter_positive(self):
        self.assertEqual(triangle_perimeter(10, 10, 10), 30)
        self.assertEqual(triangle_perimeter(4, 12, 14), 30)

    def test_perimeter_zero(self):
        self.assertEqual(triangle_perimeter(0, 10, 10), 20)


