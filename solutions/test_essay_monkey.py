import unittest
import os
from essay_monkey import *


class FileWordReaderTests(unittest.TestCase):
    """Tests for the ``FileWordReader`` class"""

    def setUp(self):

        self.nouns_filename = "nouns.txt"
        with open(self.nouns_filename, 'w') as f:
            f.write("time,year,thing,woman")

    def tearDown(self):
        try:
            os.remove(self.nouns_filename)
        except:
            pass

    def test_read_words_runs(self):
        reader = FileWordReader()

        reader.read_words("nouns.txt")

    def test_no_deletion(self):
        reader = FileWordReader()

        reader.read_words(self.nouns_filename)

        self.assertTrue(os.path.exists(self.nouns_filename))

    def test_word_contents(self):
        reader = FileWordReader()
        expected = {"time", "year", "thing", "woman"}

        actual = reader.read_words(self.nouns_filename)

        self.assertEqual(expected, actual)


class FakeWordReader:
    def __init__(self, words):
        self._words = words

    def read_words(self, filename):
        return self._words

class EssayMonkeyTests(unittest.TestCase):
    """Tests for the ``EssayMonkey`` class"""

    def test_write_essay_runs(self):
        monkey = EssayMonkey(1, 1, "", word_reader=FakeWordReader({"test"}))

        monkey.write_essay()

    def test_write_essay_returns_string(self):
        monkey = EssayMonkey(1, 1, "", word_reader=FakeWordReader({"test"}))

        actual = monkey.write_essay()

        self.assertIsInstance(actual, str)

    def test_one_sentence(self):
        monkey = EssayMonkey(1, 1, "", word_reader=FakeWordReader({"test"}))
        expected = 1

        actual = monkey.write_essay().count('.')

        self.assertEqual(expected, actual)

    def test_three_sentence(self):
        monkey = EssayMonkey(1, 3, "", word_reader=FakeWordReader({"test"}))
        expected = 3

        actual = monkey.write_essay().count('.')

        self.assertEqual(expected, actual)

    def test_nine_sentence(self):
        monkey = EssayMonkey(3, 3, "", word_reader=FakeWordReader({"test"}))
        expected = 9

        actual = monkey.write_essay().count('.')

        self.assertEqual(expected, actual)

    def test_essay_contains_test(self):
        monkey = EssayMonkey(1, 1, "", word_reader=FakeWordReader({"test"}))
        expected = "test"

        actual = monkey.write_essay()

        self.assertIn(expected, actual)


if __name__ == '__main__':
    unittest.main()
