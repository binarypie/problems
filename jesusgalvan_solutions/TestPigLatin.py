#!/usr/bin/python

# -------
# imports
# -------
from unittest import main, TestCase
from pig_latin import translate_vowel, translate_consonant, translate, contains_way, pig_latin

class TestCommonString (TestCase):
	def test_pl_1 (self):
		r = pig_latin("Gotta catch them all!")
		expected = "Ottagay atchcay hemtay allway!"
		self.assertEqual(r,  expected)
	def test_pl_2 (self):
		r = pig_latin("Bellsprout")
		expected = "Ellsproutbay"
		self.assertEqual(r,  expected)
	def test_t_1 (self):
		r = translate("Moltres")
		expected = "Oltresmay"
		self.assertEqual(r,  expected)
	def test_t_2 (self):
		r = translate("Blastoise")
		expected = "Lastoisebay"
		self.assertEqual(r,  expected)
	def test_cw_1 (self):
		r = contains_way("Weezing")
		expected = False
		self.assertEqual(r,  expected)
	def test_cw_2 (self):
		r = contains_way("gateway")
		expected = True
		self.assertEqual(r,  expected)
	def test_tv_1 (self):
		r = translate_vowel("allow")
		expected = "allowway"
		self.assertEqual(r,  expected)
	def test_tv_2 (self):
		r = translate_vowel("air")
		expected = "airway"
		self.assertEqual(r,  expected)
	def test_tc_1 (self):
		r = translate_consonant("Stomping")
		expected = "Tompingsay"
		self.assertEqual(r,  expected)
	def test_tc_2 (self):
		r = translate_consonant("running")
		expected = "unningray"
		self.assertEqual(r,  expected)

# ----
# main
# ----

main()