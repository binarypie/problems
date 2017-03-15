#!/usr/bin/python

import sys

def pig_latin(s_to_translate):
	# Break up this sentence with space as a delimeter, generate a list, and translate each word
	words = s_to_translate.split(" ")
	pig_latin_words = []
	for w in words:
		if "-" in w:
			front,end = w.split("-")
			pig_latin_s = translate(front)+"-"+translate(end)
		else:
			pig_latin_s = translate(w)
		pig_latin_words.append(pig_latin_s)
		pig_latin_words.append(" ")
	return ''.join(pig_latin_words)


def translate(w):
	pl_word = ""
	# Determine which kind of word this is and translate it
	if len(w) == 0:
		return ""
	if len(w) == 1:
		return w
	elif(contains_way(w)):
		return w
	elif w[0].lower() in 'aeiou':
		return translate_vowel(w)
	elif w[0].lower() in ' bcdfghjklmnpqrstvwxyz':
		return translate_consonant(w)
	return w

def contains_way(w):
	#check if the word ends in way, need to ignore punctuation
	index  = (w.lower()).find("way")
	if index != -1:
		if(w == "way"):
			return True
		elif(index == len(w)-3):
			return True
		elif(w[-1:] in "\!,.?';:`%/"+'"') and (index == len(w)-4):
			return True
	return False

def translate_vowel(w):
	punctuation = {}
	w_wo_punctuation = []
	for index, c in enumerate(w):
		if (c in "\,!.?';:`%/"+'"'):
			punctuation[(len(w)-index-1)] = c
		else:
			w_wo_punctuation.append(c)
	result = []
	front = w_wo_punctuation
	end = 'way'
	result.extend(front)
	result.extend(end)
	for k in sorted(punctuation):
		if(k == 0):
			result.append(punctuation[k])
		else:
			result.insert(k*-1, punctuation[k])
	return ''.join(result)



def translate_consonant(w):
	punctuation = {}
	capitalized = []
	w_wo_punctuation = []
	for index, c in enumerate(w):
		if (c in "\,!.?';:`%/"+'"'):
			punctuation[(len(w)-index-1)] = c
		elif(c.isupper()):
			capitalized.append(index)
			w_wo_punctuation.append(c.lower())
		else:
			w_wo_punctuation.append(c)
	result = []
	front = w_wo_punctuation[1:]
	middle = w_wo_punctuation[0]
	end = 'ay'
	result.extend(front)
	result.extend(middle)
	result.extend(end)
	for k in sorted(punctuation):
		if(k == 0):
			result.append(punctuation[k])
		else:
			result.insert(k*-1, punctuation[k])
	for i in capitalized:
		result[i] = result[i].upper()
	return ''.join(result)

def main(s_to_translate):
    result = pig_latin(s_to_translate)
    print(result)

if __name__ == '__main__':
    main(sys.argv[1])