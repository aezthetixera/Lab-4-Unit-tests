import unittest
import math

from circle import circle_area, circle_perimeter
from rectangle import rectangle_area, rectangle_perimeter
from square import square_area, square_perimeter
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


class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(10, 10), 100)
        self.assertEqual(rectangle_area(1, 10), 10)
        self.assertEqual(rectangle_area(0, 10), 0)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(10, 10), 40)
        self.assertEqual(rectangle_perimeter(1, 10), 22)


class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(10), 100)
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(1), 1)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(10), 40)
        self.assertEqual(square_perimeter(0), 0)


class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(1), math.pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(10), 100 * math.pi)

    def test_perimeter(self):
        self.assertEqual(circle_perimeter(1), 2 * math.pi)
        self.assertEqual(circle_perimeter(10), 20 * math.pi)
        self.assertEqual(circle_perimeter(0), 0)
    

unittest.main()