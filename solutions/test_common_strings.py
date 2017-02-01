import unittest
from common_strings import *


class CommonStringTests(unittest.TestCase):
    """Tests for the ``longest_common_string()`` function"""

    def test_function_runs(self):
        longest_common_string("", "")

    def test_returns_string(self):
        actual = longest_common_string("", "")

        self.assertIsInstance(actual, str)

    def test_matching_strings_return_same_value(self):
        input_str = "Why, hello there"

        actual = longest_common_string(input_str, input_str)

        self.assertEqual(input_str, actual)

    def test_one_empty_string_returns_empty(self):
        input1 = "calculator"
        input2 = ""
        expected = ""

        actual = longest_common_string(input1, input2)

        self.assertEqual(expected, actual)

    def test_substring_superstring_returns_substring(self):
        input1 = "cat"
        input2 = "caterpillar"
        expected = "cat"

        actual = longest_common_string(input1, input2)

        self.assertEqual(expected, actual)

    def test_start_match(self):
        input1 = "123569"
        input2 = "123456789"
        expected = "123"

        actual = longest_common_string(input1, input2)

        self.assertEqual(expected, actual)

    def test_middle_match(self):
        input1 = "14569"
        input2 = "123456789"
        expected = "456"

        actual = longest_common_string(input1, input2)

        self.assertEqual(expected, actual)

    def test_end_match(self):
        input1 = "145789"
        input2 = "123456789"
        expected = "789"

        actual = longest_common_string(input1, input2)

        self.assertEqual(expected, actual)

    def test_single_character_match(self):
        input1 = "a"
        input2 = "exceptional"
        expected = "a"

        actual = longest_common_string(input1, input2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
