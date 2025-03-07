import unittest
from algorithms.countValidTriangles import countValidTriangles


class TestCountValidTriangles(unittest.TestCase):
    def test_valid_triangles(self):
        self.assertEqual(countValidTriangles([4, 6, 3, 7]), 3)  # Triángulos: (3, 4, 6), (3, 6, 7), (4, 6, 7)
        self.assertEqual(countValidTriangles([10, 21, 22, 100, 101, 200, 300]), 6)
        self.assertEqual(countValidTriangles([5, 5, 5, 5]), 4)
        self.assertEqual(countValidTriangles([2, 2, 3, 3]), 4)  #  (2, 2, 3), (2, 3, 3), (2, 2, 3), (2, 3, 3), (2, 3, 3)

    def test_no_valid_triangles(self):
        self.assertEqual(countValidTriangles([1, 2, 3]), 0)
        self.assertEqual(countValidTriangles([1, 1, 2]), 0)
        self.assertEqual(countValidTriangles([10, 20, 30, 40]), 1)

    def test_less_than_three_sides(self):
        self.assertEqual(countValidTriangles([]), 0)
        self.assertEqual(countValidTriangles([1]), 0)
        self.assertEqual(countValidTriangles([1, 2]), 0)

    def test_duplicate_sides(self):
        self.assertEqual(countValidTriangles([3, 3, 3, 3, 3]), 10)
        self.assertEqual(countValidTriangles([2, 2, 3, 3, 4, 4]), 18)

    def test_large_numbers(self):
        self.assertEqual(countValidTriangles([1000, 2000, 3000, 4000, 5000]), 3)
        self.assertEqual(countValidTriangles([100000, 200000, 300000, 400000]), 1)

