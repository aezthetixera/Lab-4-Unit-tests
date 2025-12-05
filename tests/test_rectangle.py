import unittest

from rectangle import rectangle_area, rectangle_perimeter


class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(10, 10), 100)
        self.assertEqual(rectangle_area(1, 10), 10)
        self.assertEqual(rectangle_area(0, 10), 0)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(10, 10), 40)
        self.assertEqual(rectangle_perimeter(1, 10), 22)



