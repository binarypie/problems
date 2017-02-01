import unittest
import os
from utility import FileReader


class FileReaderTests(unittest.TestCase):

    def setUp(self):
        self.test_filename = "test.txt"
        self.test_file_contents = "Test file for logs.FileReader"

        with open(self.test_filename, 'w') as f:
            f.write(self.test_file_contents)

    def tearDown(self):
        try:
            os.remove(self.test_filename)
        except:
            pass

    def test_read_file_runs(self):
        reader = FileReader()

        reader.read_file(self.test_filename)

    def test_no_deletion(self):
        reader = FileReader()

        reader.read_file(self.test_filename)

        self.assertTrue(os.path.exists(self.test_filename))

    def test_reads_file(self):
        reader = FileReader()
        expected = self.test_file_contents

        actual = reader.read_file(self.test_filename)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()