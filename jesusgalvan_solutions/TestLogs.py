#!/usr/bin/python

# -------
# imports
# -------
from unittest import main, TestCase
from common_string import *

class TestCommonString (TestCase):
    def test_cs_1 (self):
        r = longest_common_substring("charmender", "armando")
        expected = "arm"
        self.assertEqual(r,  expected)
    def test_cs_2 (self):
        r = longest_common_substring("", "   ")
        expected = ""
        self.assertEqual(r,  expected)
    def test_cs_3 (self):
        r = longest_common_substring("charmender", "gyrados")
        expected = "a"
        self.assertEqual(r,  expected)
    def test_cs_4 (self):
        r = longest_common_substring("charmeleon", "charizard")
        expected = "char"
        self.assertEqual(r,  expected)

# ----
# main
# ----

main()