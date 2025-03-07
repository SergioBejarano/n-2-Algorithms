import unittest
from algorithms.findAllPairs import findAllPairs

class TestFindAllPairs(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(findAllPairs([]), [])

    def test_single_element(self):
        self.assertEqual(findAllPairs([1]), [])

    def test_two_elements(self):
        self.assertEqual(findAllPairs([1, 2]), [(1, 2)])

    def test_multiple_elements(self):
        self.assertEqual(findAllPairs([1, 2, 3]), [(1, 2), (1, 3), (2, 3)])
        self.assertEqual(findAllPairs([4, 5, 6, 7]), [(4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7)])

    def test_duplicate_elements(self):
        self.assertEqual(findAllPairs([1, 1, 2]), [(1, 1), (1, 2), (1, 2)])
        self.assertEqual(findAllPairs([2, 2, 2]), [(2, 2), (2, 2), (2, 2)])

    def test_large_array(self):
        large_array = list(range(100))
        result = findAllPairs(large_array)
        self.assertEqual(len(result), 4950)
