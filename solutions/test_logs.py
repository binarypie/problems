import unittest
from logs import *


class FakeFileReader:
    def __init__(self, echo_text):
        self._echo_text = echo_text

    def read_file(self, filename):
        return self._echo_text


class LogReaderTests(unittest.TestCase):
    def test_read_log_runs(self):
        reader = LogReader(file_reader=FakeFileReader("test"))

        reader.read_log("")

    def test_read_log_returns_list(self):
        reader = LogReader(file_reader=FakeFileReader("test"))

        actual = reader.read_log("")

        self.assertIsInstance(actual, list)

    def test_read_log_returns_one(self):
        reader = LogReader(file_reader=FakeFileReader("test"))
        expected = 1

        actual = len(reader.read_log(""))

        self.assertEqual(expected, actual)

    def test_read_log_returns_three(self):
        reader = LogReader(file_reader=FakeFileReader("test\ntest\ntest"))
        expected = 3

        actual = len(reader.read_log(""))

        self.assertEqual(expected, actual)

    def test_read_log_correct_entry(self):
        reader = LogReader(file_reader=FakeFileReader("test"))

        actual = reader.read_log("")[0].entry()

        self.assertEqual(actual, "test")

    def test_read_log_correct_entries(self):
        reader = LogReader(file_reader=FakeFileReader("one\ntwo\nthree"))
        expected = "three"

        actual = reader.read_log("")[2].entry()

        self.assertEqual(expected, actual)


class LogItemTests(unittest.TestCase):
    def setUp(self):
        self.test_log_string = '111.1.1.1 [01/Jan/2017:00:00:00] ' \
                               '"TEST /TEST.test HTTP/1.1" 200 0 "http://test.com/tester" '

    def test_object_builds(self):
        LogItem("")

    def test_contains_log_entry(self):
        log_item = LogItem("")
        expected = ""

        actual = log_item.entry()

        self.assertEqual(expected, actual)

    def test_contains_ip(self):
        log_item = LogItem(self.test_log_string)
        expected = "111.1.1.1"

        actual = log_item.ip()

        self.assertEqual(expected, actual)

    def test_contains_date(self):
        log_item = LogItem(self.test_log_string)
        expected = "01/Jan/2017"

        actual = log_item.date()

        self.assertEqual(expected, actual)

    def test_contains_time(self):
        log_item = LogItem(self.test_log_string)
        expected = "00:00:00"

        actual = log_item.time()

        self.assertEqual(expected, actual)

    def test_contains_file(self):
        log_item = LogItem(self.test_log_string)
        expected = "TEST.test"

        actual = log_item.file()

        self.assertEqual(expected, actual)

    def test_contains_referer(self):
        log_item = LogItem(self.test_log_string)
        expected = "http://test.com/tester"

        actual = log_item.referrer()

        self.assertEqual(expected, actual)


# class LogSearchTests(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
