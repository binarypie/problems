import random
import unittest
import os


class FileWordReader:
    def read_words(self, filename):
        with open(filename, 'r') as f:
            lines = f.read().splitlines()

        words = set()
        for line in lines:
            line_words = line.split(',')
            words.update(line_words)

        return words


class EssayMonkey:
    """A class that writes essays of variable sentence and paragraph count. Pool of words comes
        from external files"""
    def __init__(self, paragraph_count, sentence_count, *files, word_reader=FileWordReader()):
        if not isinstance(paragraph_count, int):
            raise ValueError("paragraph_count input '{}' is not an integer".format(paragraph_count))

        if not isinstance(sentence_count, int):
            raise ValueError("sentence_count input '{}' is not an integer".format(sentence_count))

        if len(files) < 1:
            raise ValueError("No word files were provided")

        self._paragraph_count = paragraph_count
        self._sentence_count = sentence_count

        words = set()
        for file in files:
            words.update(word_reader.read_words(file))

        self._words = words

    def write_essay(self):
        """Produces an essay based on the current paragraph and sentence counts, using the words
            provided when the object was created"""
        essay = ""
        words_count = len(self._words)

#        for _ in range(self._paragraph_count):
#            for _ in range(self._sentence_count):


        return essay

    def set_paragraph_count(self, paragraph_count):
        self._paragraph_count = paragraph_count

    def set_sentence_count(self, sentence_count):
        self._sentence_count = sentence_count


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
        monkey = EssayMonkey(1, 1, "", word_reader=FakeWordReader(set()))

        monkey.write_essay()

    def test_write_essay_returns_string(self):
        monkey = EssayMonkey(1, 1, "", word_reader=FakeWordReader(set()))

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


if __name__ == '__main__':
    unittest.main()
