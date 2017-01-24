# call: python PigLatin.py arg0
# param arg0: The string to be translated
# 
# Translates a string into pig latin based on the rules
# specified on the document and prints it out
#
# ie: python PigLatin.py "I'm Lo-vin' 'eM" -> Imwa'y oLay-invay' eMw'ay
# Author: Jie Luo

import sys
import re

vowels = ['a', 'e', 'i', 'o', 'u']
punctuation = re.compile("[^\w]")
spaces = re.compile("\s|-")


# Takes in length, the word, and whether it starts with a vowel
# and translated it into pig latin. Takes in these values to save runtime
# since we already know length and whether it starts with vowel
#
# param length: int length of the word
# param word: string of the word to be translated
# param startsWithVowel: boolean whether or not word starts with vowel
#
# returns: translated string
def translateWord(length, word, startsWithVowel) :
    stackHead = 0
    addition = ""
    start = 0
    firstLetter = word[0]

    if startsWithVowel:
        addition = "way"
        start = 0
    else : 
        addition = "ay"
        start = 1

    wordBuffer = [None] * (length + len(addition))
    for i in range(start, length) :
        charAtIndex = word[i]
        if punctuation.match(charAtIndex) :
            distFromEnd = length - i
            wordBuffer[length + len(addition) - distFromEnd] = charAtIndex
        else :
            while wordBuffer[stackHead] : 
                stackHead += 1
            wordBuffer[stackHead] = charAtIndex

    # add first letter back if needed
    if not startsWithVowel : 
        while wordBuffer[stackHead] : 
            stackHead += 1
        wordBuffer[stackHead] = firstLetter

    for letter in addition :
        while wordBuffer[stackHead] : 
            stackHead += 1
        wordBuffer[stackHead] = letter

    return ''.join(wordBuffer)


# Takes in a word and decides how to translate it based on first letter
# Uses translateWord(length, word, startsWithVowel)
#
# param word: word to be translated
#
# returns: translated string
def manageWord(word) :
    length = len(word)
    if length == 1:
        return word
        next

    firstLetter = word[0]
    # case where punctuation starts off word
    if punctuation.match(firstLetter) : 
        for i in range(1, length):
            if not punctuation.match(word[i]) and word[i] in vowels:         
                    translated = translateWord(length, word, True)    
                    return(translated)
    # case where first letter is vowel
    elif firstLetter.lower() in vowels :
        translated = translateWord(length, word, True)    
        return(translated)
    # case where first letter is consonant
    else :
        translated = translateWord(length, word, False)    
        return(translated)


result = []

# Split the words by space and then by hyphen
words = sys.argv[1].split()
for wordsHypen in words :
    splitWords = wordsHypen.split('-') 
    # handle space-split words and hyphen-split separately
    if len(splitWords) > 1 :
        subResult = []
        for word in splitWords:
            translated = manageWord(word)
            subResult.append(translated)
        result.append('-'.join(subResult));
    else:
        translated = manageWord(wordsHypen)
        result.append(translated)

print " ".join(result)
