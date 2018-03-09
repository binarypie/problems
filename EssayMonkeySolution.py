import sys
import random

if (len(sys.argv) != 3):
    print "Incorrect number of arguments. \n Usage: python EssayMonkeySolution.py <num of paragraphs> <num of sentences per paragraph>"
    exit(1)

numOfParagraphs = int(sys.argv[1])
sentencesPerParagraph = int(sys.argv[2])

adjectivesPath = "EssayMonkeyAdjectives.txt"
adjectives = [x.strip() for x in open(adjectivesPath, 'r').read().split(',')]

nounsPath = "EssayMonkeyNouns.txt"
nouns = [x.strip() for x in open(nounsPath, 'r').read().split(',')]

verbsPath = "EssayMonkeyVerbs.txt"
verbs = [x.strip() for x in open(verbsPath, 'r').read().split(',')]

minSentenceLen = 3
maxSentenceLen = 8

def makeEssay(numParagraphs):
	paraArr = []

	paraCount = 0
	while paraCount < numParagraphs:
		paraArr.append(makeParagraph(sentencesPerParagraph))
		paraCount += 1

	return '\n'.join(paraArr)

def makeParagraph(numSentences):
	sentenceArr = []

	sentenceCount = 0
	while sentenceCount < numSentences:
		sentenceArr.append(makeSentence(minSentenceLen, maxSentenceLen))
		sentenceCount += 1

	indent = '    '

	return indent + ' '.join(sentenceArr)

'''
Every sentence is made up of an adjective, noun, and verb in that order. 

Therefore, a sentence of length 5 will be: adjective+noun+verb+adjective+noun.

The first letter of the sentence is capitalized, and all sentences end with a period.
'''
def makeSentence(minLen, maxLen):
	res = []
	sentenceLengths = [x for x in range(minLen, maxLen+1)]
	length = random.choice(sentenceLengths)

	wordCount = 0
	while wordCount < length:
		if wordCount % 3 == 0:
			if wordCount == 0:
				res.append(random.choice(adjectives).capitalize())
			else:
				res.append(random.choice(adjectives))
		elif wordCount % 3 == 1:
			res.append(random.choice(nouns))
		else:
			res.append(random.choice(verbs))

		wordCount += 1

	return ' '.join(res)+'.'

print makeEssay(numOfParagraphs)