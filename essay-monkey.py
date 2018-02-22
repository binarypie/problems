# Library imports
import sys
import random

# Constants
WHITESPACE = " \n \t"
PRONOUNS = ["I","you","he", "she", "this", "it"]
ARTICLES = ["the", "a", "an", "your","my","his","her","its"]
HELPING_VERBS = ["has", "am", "is"]
CONJUNCTIONS = [" while", " even though", " even if", " if", " although", " then", " and", " but", " or", " so",","," -",":",";"]

# Given a string :word, remove any succeeding and preceeding whitespace. Return modified string.
def removeWhitespace(word):
	while len(word) > 0 and word[0] in WHITESPACE:
		word = word[1:]
	while len(word) > 0 and word[-1] in WHITESPACE:
		word = word[:-1]
	return word

# Given a file :filename, parse its comma-separated contents and return a list of strings with no preceeding/succeeding whitespaces.
def parseFile(filename):
	wordFile = open(filename,"r")
	wordList = []
	for line in wordFile:
		words = line.split(',')
		for word in words:
			word = removeWhitespace(word)
			if '/' in word:
				wordList = wordList + word.split('/')
			elif '(' in word and ')' in word:
				words.remove(word)
				head, option = word.split(' ')
				option = head + " " + option[1:-1]
				wordList = wordList + [head, option]
			else:
				if len(word) > 0: wordList.append(word)
	wordFile.close()
	return wordList

# More constants!
VERBS = parseFile("EssayMonkeyVerbs.txt")
NOUNS = parseFile("EssayMonkeyNouns.txt")
ADJECTIVES = parseFile("EssayMonkeyAdjectives.txt")

# Return a random element from :wordList
def getRandomWord(wordList):
	return wordList[random.randint(0,len(wordList)-1)]

# Return a grammatically correct form of :phrase.
# Returned value will never have "an" before a consonant or "a" before a vowel.
def fixPhraseGrammar(phrase):
	# Make sure "an" is always before a 
	if " an " in phrase:
		pre,post = phrase.split(" an ")
		if post[0] not in "AaEeIiOoUu":
			phrase = pre + " a " + post
	if " a " in phrase:
		pre,post = phrase.split(" a ")
		if post[0] in "AaEeIiOoUu":
			phrase = pre + " an " + post

	return phrase

# Return a randomly generated subject for a sentence.
def subject():
	form = random.randint(0,1)
	adj = random.randint(0,1)
	subject = ""
	if form == 0:
		subject += getRandomWord(PRONOUNS)
	elif form == 1:
		subject += getRandomWord(ARTICLES) + " "
		if adj == 1: subject += getRandomWord(ADJECTIVES) + " "
		subject += getRandomWord(NOUNS)
	return subject

# Return a randomly generated verb phrase for a sentence.
def verbPhrase():
	form = random.randint(0,1)
	adj = random.randint(0,1)
	verbPhrase = ""
	if form == 0: verbPhrase += getRandomWord(VERBS)
	if form == 1:
		verbPhrase += getRandomWord(VERBS) + " " + getRandomWord(ARTICLES) + " "
		if adj == 1: verbPhrase += getRandomWord(ADJECTIVES) + " "
		verbPhrase += getRandomWord(NOUNS)
	return verbPhrase

# Return a grammatically correct phrase using randomly generated subject and verb phrase.
def phraseGenerator():
	return fixPhraseGrammar(subject() + " " + verbPhrase())

# Return a grammatically correct form of :sentence
# Return value will have an upper case first character and a period (.) at the end.
def fixSentenceGrammar(sentence):
	return sentence[0].upper() + sentence[1:] + ". "

# Construct a grammatically correct essay with :noOfParas paragraphs, each with :sentencesPerPara paragraphs, and write it to :outfilename.txt.
def writeEssay(noOfParas, sentencesPerPara, outfilename):
	file = open(outfilename,"w")
	for paraNo in range(noOfParas):
		para = "\t"
		for sentenceNo in range(sentencesPerPara):
			sentence = phraseGenerator() 
			i = random.randint(0,1)
			if i == 1:
				sentence += getRandomWord(CONJUNCTIONS) + " " + phraseGenerator()
			para += fixSentenceGrammar(sentence)
		para += "\n"
		file.write(para)
	print("Essay saved in " + outfilename + "!")
	file.close()

# Main
noOfParas = int(sys.argv[1])
sentencesPerPara = int(sys.argv[2])
outfilename = sys.argv[3]

writeEssay(noOfParas, sentencesPerPara, outfilename)


