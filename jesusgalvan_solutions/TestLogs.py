#!/usr/bin/python

# -------
# imports
# -------
from io       import StringIO
from unittest import main, TestCase
from logs import search_browser, search_os, search_date, search_time, print_results,\
search_file, search_ip, version, search_referrer, load_logs

class TestLogs (TestCase):
    def test_search_os(self):
        r = search_os("Android")
        expected = True
        b = False
        if r:
            b = True
        self.assertEqual(b,  expected)
    def test_search_browser(self):
        r = search_browser("Chrome")
        expected = True
        b = False
        if r:
            b = True
        self.assertEqual(b,  expected)
    def test_search_file(self):
        r = search_file("0xb.jpg")
        expected = True
        b = False
        if r:
            b = True
        self.assertEqual(b,  expected)
    def test_search_ip(self):
        r = search_ip("127.0.0.1")
        expected = True
        b = False
        if r:
            b = True
        self.assertEqual(b,  expected)
    def test_search_date(self):
        r = search_date("19/Jun/2012")
        expected = True
        b = False
        if r:
            b = True
        self.assertEqual(b,  expected)
    def test_search_time(self):
        r = search_time("09:16:22")
        expected = True
        b = False
        if r:
            b = True
        self.assertEqual(b,  expected)
    def test_search_referrer (self):
        r = search_referrer("http://domain.com/azb")
        expected = True
        b = False
        if r:
            b = True
        self.assertEqual(b,  expected)
    def test_version (self):
        r = version()
        self.assertEqual(r, None)
    def test_load_logs (self):
        r = load_logs("logs.txt")
        expected = True
        b = False
        if r:
            b = True
        self.assertEqual(b,  expected)
    def test_print_results (self):
        r = print_results([1])
        self.assertEqual(r,  None)

# ----
# main
# ----

main()