# Thomas Doan
# EssayMonkey.py
# 10/30/15
# Creates essay based on user given paragraph and sentence amount.

import random

'''
Main function accepts user amount of paragraphs and sentences.
Calls auxiliary function to create essay based on these amounts.
'''

"""
Reads from the provided text files and makes lists with the words
in the files. Using these lists, makes an "essay" with user given
paragraph and sentence amount.
Args:
numParagraphs: The user given amount of paragraphs desired in essay.
numSentences: The user given amount of sentences desired in essay.
Returns:
A randomly generated essay string with the given amount
of paragraphs and sentences.
"""


def essayMonkey(numParagraphs, numSentences):
    # Creates lists from provided text files
    essay = ""
    nounsList = open("EssayMonkeyNouns.txt")
    verbsList = open("EssayMonkeyVerbs.txt")
    adjectivesList = open("EssayMonkeyAdjectives.txt")

    nouns = nounsList.read().strip("\n").split(",")
    verbs = verbsList.read().strip("\n").split(",")
    adjectives = adjectivesList.read().strip("\n").split(",")

    nounsList.close()
    verbsList.close()
    adjectivesList.close()

    # Loops until desired amount of paragraphs are present
    i = 0
    while i < numParagraphs:
        j = 0
        paragraph = "    "
        while j < numSentences:
            paragraph += createSentence(nouns, verbs, adjectives)
            j += 1
        if i == (numParagraphs - 1):
            essay += paragraph
        else:
            essay += paragraph + "\n" + "\n"
        i += 1

    return essay

"""
Creates a sentence string using the given lists of nouns, verbs, and adjectives.
Chooses a random amount of adjectives, as well as a random noun and verb.
Args:
nouns: List of nouns present in the text file
verbs: List of verbs present in the text file
adjectives: List of adjectives present in the text file
Returns:
A sentence string with a random length based off the amount of added
adjectives.
"""


def createSentence(nouns, verbs, adjectives):
    sentence = ""
    randNum = random.random()

    # Adds a random number of adjectives to the sentence
    while randNum < 0.7:
        sentence = sentence + random.choice(adjectives) + " "
        randNum = random.random()

    sentence += random.choice(nouns) + " "
    sentence += random.choice(verbs) + " "

    # Capitalize first letter
    sentence = sentence[0].capitalize() + sentence[1:len(sentence)-1] + "." + " "

    return sentence

numParagraphs = input("Number of paragraphs: ")
numSentences = input("Number of sentences: ")
essay = essayMonkey(int(numParagraphs), int(numSentences))
print(essay)
