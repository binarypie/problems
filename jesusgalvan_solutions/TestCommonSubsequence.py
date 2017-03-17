#!/usr/bin/python

# -------
# imports
# -------
from unittest import main, TestCase
from common_subsequence import find_lcs, longest_common_subsequence

class TestCommonString (TestCase):
	def test_cs_1 (self):
		r = longest_common_subsequence("common_subsequence_SAMPLE.txt")
		expected = ['MJAU']
		self.assertEqual(r,  expected)
	def test_cs_2 (self):
		r = find_lcs("", "")
		expected = ""
		self.assertEqual(r,  expected)
	def test_cs_3 (self):
		r = find_lcs("charmender", "gyrados")
		expected = "ad"
		self.assertEqual(r,  expected)
	def test_cs_4 (self):
		r = find_lcs("charmeleon", "charizard")
		expected = "char"
		self.assertEqual(r,  expected)

# ----
# main
# ----
main()