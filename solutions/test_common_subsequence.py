import unittest
import os
from common_subsequence import *

class CommonStringTests(unittest.TestCase):
    """Tests for the ``longest_common_subsequence`` function"""

    def setUp(self):
        self.empty_filename = "empty_test_file.txt"
        with open(self.empty_filename, 'w') as f:
            f.write("")

        self.filename = "common_subsequence_test_file.txt"
        with open(self.filename, 'w') as f:
            f.write("123;123\n"
                    "\n"
                    "\n"
                    "1234;5678\n"
                    "asdf1ghj2kl3;qwe1rty2uio3\n"
                    "\n"
                    "a1s2d3f4g5h;a1s2d3h4g5f\n"
                    "XMJYAUZ;MZJAWXU\n")

        self.oversized_filename = "oversized_subsequence_test_file.txt"
        with open(self.oversized_filename, 'w') as f:
            f.write("123456789012345678901234567890123456789012345678901;it's too long! D:")

    def tearDown(self):
        try:
            os.remove(self.empty_filename)  # Subsequent files would not be deleted if the first raises an exception
            os.remove(self.filename)
            os.remove(self.oversized_filename)
        except:
            pass

    def test_function_runs(self):
        longest_common_subsequence(self.filename)

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            longest_common_subsequence("foobar")

    def test_no_deletion(self):
        longest_common_subsequence(self.filename)
        self.assertTrue(os.path.exists(self.filename))

    def test_empty_file(self):
        expected = []

        actual = longest_common_subsequence(self.empty_filename)

        self.assertEqual(expected, actual)

    def test_identical_sequences(self):
        line_number = 0
        expected = "123"

        actual = longest_common_subsequence(self.filename)[line_number]

        self.assertEqual(expected, actual)

    def test_disjoint_sequences(self):
        line_number = 1
        expected = ""

        actual = longest_common_subsequence(self.filename)[line_number]

        self.assertEqual(expected, actual)

    def test_matching_sequences(self):
        line_number = 2
        expected = "123"

        actual = longest_common_subsequence(self.filename)[line_number]

        self.assertEqual(expected, actual)

    def test_mostly_similar_sequences(self):
        line_number = 3
        expected = "a1s2d34g5"

        actual = longest_common_subsequence(self.filename)[line_number]

        self.assertEqual(expected, actual)

    def test_example_sequences(self):
        line_number = 4
        expected = "MJAU"

        actual = longest_common_subsequence(self.filename)[line_number]

        self.assertEqual(expected, actual)

    def test_long_sequences(self):
        actual = longest_common_subsequence(self.oversized_filename)

        self.assertLess(len(actual), 1)

if __name__ == '__main__':
    unittest.main()
