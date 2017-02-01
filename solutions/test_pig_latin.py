import unittest
import re
from pig_latin import *


class PigLatinTests(unittest.TestCase):
    """Tests for the ``pig_latin()`` function"""

    def test_function_runs(self):
        pig_latin("")

    def test_returns_string(self):
        actual = pig_latin("")

        self.assertIsInstance(actual, str)

    def test_empty_string_empty(self):
        actual = pig_latin("")

        self.assertEqual("", actual)

    def test_single_word(self):
        expected = "atcay"

        actual = pig_latin("cat")

        self.assertEqual(expected, actual)

    def test_two_words(self):
        expected = "adbay ogday"

        actual = pig_latin("bad dog")

        self.assertEqual(expected, actual)

    def test_hyphen_word(self):
        expected = "pidersay-rabcay"

        actual = pig_latin("spider-crab")

        self.assertEqual(expected, actual)

    def test_retains_word_count(self):
        expected = 5

        actual = len(re.split(r"[ -]+", pig_latin("test test test-test test")))

        self.assertEqual(expected, actual)

    def test_single_letters_unchanged(self):
        input_str = "a b c d e"
        expected = input_str

        actual = pig_latin(input_str)

        self.assertEqual(expected, actual)

    def test_vowel_words(self):
        input_str = "enigmatic owls"
        expected = "enigmaticway owlsway"

        actual = pig_latin(input_str)

        self.assertEqual(expected, actual)

    def test_way_words(self):
        input_str = "hemingway away"
        expected = "hemingway away"

        actual = pig_latin(input_str)

        self.assertEqual(expected, actual)

    def test_punctuation_placement(self):
        input_str = "andre' shouldn't"
        expected = "andreway' houldntsa'y"

        actual = pig_latin(input_str)

        self.assertEqual(expected, actual)

    def test_capitalization_indexes(self):
        input_str = "BoO lUIgI"
        expected = "OoBay uIGiLay"

        actual = pig_latin(input_str)

        self.assertEqual(expected, actual)

    def test_example(self):
        input_str = "HeLLo World! I can't wait to explore your VAST forests. The-End!"
        expected = "ElLOhay Orldway! I antca'y aitway otay exploreway ouryay ASTVay orestsfay. Hetay-Endway!"

        actual = pig_latin(input_str)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
