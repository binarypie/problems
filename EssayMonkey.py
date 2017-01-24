# call: python EssayMonkey.py arg0 arg1
# param arg0: integer number of paragraphs to be generated
# param arg1: integer number of sentences per paragraph
#
# There are many ways to structure sentences given noun, verb, adj. 
# The simplest is noun verb. Before every noun, there can be multiple adjectives
# I decided to have more fun and add conjunctions. Whether nouns have adjectives 
# or sentences have conjunctions depends on a random distribution. The files
# EssayMonkeyVerbs.txt, EssayMonkeyNouns.txt, EssayMonkeyAdjectives.txt
# must be in the same directory as this file
#
# Author: Jie Luo

import sys
import random
import re

verbs = open('EssayMonkeyVerbs.txt', 'r').read().split(',')
nouns = open('EssayMonkeyNouns.txt', 'r').read().split(',')
adjectives = open('EssayMonkeyAdjectives.txt', 'r').read().split(',')
conjunctions = ["and", "for", "because", "or", "but", "while", "since", "yet",
				"so", "when"]


# Creates a clause of Adjective* Noun Verb
# returns: string of the clause created
def createClause() :
    clause = []
    numAdjToPut = int(round(random.normalvariate(1, 1)))
    if numAdjToPut < 0:
        numAdjToPut = 0
    for k in range(0, numAdjToPut):
        index = random.randint(0, numAdjectives - 1)
        clause.append(adjectives[index])
    index = random.randint(0, numNouns - 1)
    clause.append(nouns[index])
    index = random.randint(0, numVerbs - 1)
    clause.append(verbs[index])
    return clause


numParagraphs = int(sys.argv[1])
numSentences = int(sys.argv[2])

#remove duplicates
verbs = list(set(verbs))
nouns = list(set(nouns))
adjectives = list(set(adjectives))

numVerbs = len(verbs)
numNouns = len(nouns)
numAdjectives = len(adjectives)
numConjunctions = len(conjunctions)

essay = []

for i in range(0, numParagraphs):
    paragraph = []
    for j in range(0, numSentences) :
        sentence = []
        sentence.extend(createClause())

        # give 1/2 chance that sentence has conjunction
        hasConjunction = random.randint(0, 1) 
        if hasConjunction == 0:
            index = random.randint(0, numConjunctions - 1)
            sentence.append(conjunctions[index])
            sentence.extend(createClause())

        sentenceString = (" ".join(sentence))
        sentenceString = sentenceString.capitalize()
        sentenceString += "."                    
        paragraph.append(sentenceString)

    essay.append("\n\t" + " ".join(paragraph))

essayString = "".join(essay)
print essayString