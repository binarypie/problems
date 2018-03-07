import re
import sys

if (len(sys.argv) != 2):
    print "Incorrect number of arguments. \n Usage: python PigLatinSolution.py textfile"
    exit(1)

file = open(sys.argv[1],'r')
with file as myfile:
    text=myfile.read().replace('\n', '')

# takes in string, sentence, or paragraph
def translateToPigLatin(str):
	res = []
	words = str.split()
	for word in words:
		reconstructed = []
		split = re.split('([a-zA-Z\']+)', word)
		for w in split:
			if re.match('[a-zA-Z\']+', w):
				puncIndices = []
				capitalIndices = []
				saveSpecialIndices(w, puncIndices, capitalIndices)

				temp = translateWord(w)
				for p in puncIndices:
					temp = insertPunct(temp, len(w)-p[0]+1, p[1])

				temp = recapitalize(temp, capitalIndices)
				reconstructed.append(temp)
			else:
				reconstructed.append(w)

		res.append(''.join(reconstructed))

	return ' '.join(res)

def saveSpecialIndices(w, puncIndices, capitalIndices):
	for i in range(len(w)):
		if re.match('([^a-zA-Z0-9\-])', w[i]):
			puncIndices.append((len(w)-i-1, w[i]))

		if re.match('([A-Z])', w[i]):
			capitalIndices.append((i))

	return

def translateWord(word):
	# single letter
	if len(word) < 2:
		return word

	word = word.lower()
	word = stripRemainingPunct(word)

	# check for way ending
	if checkWayEnding(word):
		return word

	# check first letter
	if isFirstLetterVowel(word):
		return word+"way"
	else:
		return word[1:]+word[0]+"ay"

def stripRemainingPunct(word):
	res = ""
	for ch in word:
		if not re.match('[^a-zA-Z\-]', ch):
			res+=ch

	return res

def checkWayEnding(word):
	if len(word) >= 3:
		i = len(word)-3
		if word[i:] == "way":
			return True

	return False

def isFirstLetterVowel(word):
	vowels = ["a", "e", "i", "o", "u"]
	if word[0].lower() in vowels:
		return True

	return False

def insertPunct(word, i, punct):
	if i == 0:
		return punct + word

	return word[:i] + punct + word[i:]

def recapitalize(word, indices):
	res = ""
	for i in range(len(word)):
		if i in indices:
			res += word[i].upper()
		else:
			res += word[i]

	return res
	
print translateToPigLatin(text)
