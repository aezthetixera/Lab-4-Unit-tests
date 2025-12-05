import unittest

from square import square_area, square_perimeter


class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(10), 100)
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(1), 1)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(10), 40)
        self.assertEqual(square_perimeter(0), 0)



