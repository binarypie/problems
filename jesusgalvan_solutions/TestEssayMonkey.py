#!/usr/bin/python

# -------
# imports
# -------
from unittest import main, TestCase
from essay_monkey import provide_word_banks, generate_sentence, write_essay

class TestCommonString (TestCase):
	def test_pwb_1 (self):
		a, n, v = provide_word_banks()
		r = False
		expected = True
		if(a and n and v):
			r = True
		self.assertEqual(r,  expected)
	def test_gs_2 (self):
		v = ["run", "hide"]
		a = ["quickly", "well"]
		n = ["he", "pikachu"]
		s = generate_sentence(v,a,n)
		expected = 6
		self.assertEqual(len(s),  expected)
	def test_gs_1 (self):
		v = ["walk", "kick"]
		a = ["slowly", "surely"]
		n = ["he", "squirtle"]
		s = generate_sentence(v,a,n)
		expected = 6
		self.assertEqual(len(s),  expected)
	def test_we_1 (self):
		r = write_essay(1,1)
		expected = True
		b = False
		if("\t" in r):
			b = True
		self.assertEqual(b,  expected)
	def test_we_2 (self):
		r = write_essay(2,2)
		expected = True
		b = False
		if("\n" in r):
			b = True
		self.assertEqual(b,  expected)


# ----
# main
# ----

main()