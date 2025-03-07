import unittest
from algorithms.areAnagrams import areAnagrams

class TestAreAnagrams(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(areAnagrams("listen", "silent"))
        self.assertTrue(areAnagrams("triangle", "integral"))

    def test_not_anagrams(self):
        self.assertFalse(areAnagrams("hello", "world"))
        self.assertFalse(areAnagrams("python", "java"))
        self.assertFalse(areAnagrams("apple", "pale"))
        self.assertFalse(areAnagrams("abc", "def"))
        self.assertFalse(areAnagrams("abc", "abcd"))

    def test_case_insensitivity(self):
        self.assertTrue(areAnagrams("Listen", "Silent"))
        self.assertTrue(areAnagrams("Race", "Care"))
        self.assertTrue(areAnagrams("Tea", "Eat"))

    def test_empty_strings(self):
        self.assertTrue(areAnagrams("", ""))
        self.assertFalse(areAnagrams("", "a"))

    def test_special_characters(self):
        self.assertTrue(areAnagrams("12345", "54321"))
        self.assertTrue(areAnagrams("a1b2c3", "c3b2a1"))
        self.assertFalse(areAnagrams("a1b2c3", "a1b2c4"))
