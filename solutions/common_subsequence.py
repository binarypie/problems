import unittest
import os


def create_subsequence_matrix(x_string, y_string):
    matrix = [[0 for _ in range(len(y_string) + 1)] for _ in range(len(x_string) + 1)]

    for y in range(1, len(y_string) + 1):
        for x in range(1, len(x_string) + 1):
            if x_string[x-1] == y_string[y-1]:
                matrix[x][y] = matrix[x-1][y-1] + 1
            else:
                matrix[x][y] = max(matrix[x-1][y], matrix[x][y-1])

    return matrix


def trace_subsequence_matrix(matrix, x_string, y_string, x_index, y_index):
    if x_index == 0 or y_index == 0:
        return ''

    if x_string[x_index-1] == y_string[y_index-1]:
        return trace_subsequence_matrix(matrix, x_string, y_string, x_index-1, y_index-1)\
               + x_string[x_index-1]

    if matrix[x_index-1][y_index] > matrix[x_index][y_index-1]:
        return trace_subsequence_matrix(matrix, x_string, y_string, x_index-1, y_index)
    else:
        return trace_subsequence_matrix(matrix, x_string, y_string, x_index, y_index-1)


def longest_common_subsequence(filename):
    """Finds the longest, but not necessarily sequential, subsequence between two semicolon delimited
        strings on each line of the file specified by the input argument
    """

    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    pairs = []
    for line in lines:
        if line:
            line_split = line.split(';')
            if len(line_split[0]) < 51 and len(line_split[1]) < 51:
                pairs.append(line_split)

    return_list = []
    for pair in pairs:
        matrix = create_subsequence_matrix(pair[0], pair[1])
        longest_subsequence = trace_subsequence_matrix(matrix, pair[0], pair[1], len(pair[0]), len(pair[1]))

        return_list.append(longest_subsequence)

    return return_list


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
