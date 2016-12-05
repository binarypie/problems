# Thomas Doan
# PigLatin.py
# 10/29/15
# Translates input into Pig Latin

import string

vowels = {'a','e','i','o','u'}

'''
Main function accepts a string and returns the pig latin version.
Calls auxiliary function translate() to handle the translation.
'''

"""
Accepts a string and uses auxiliary function translate() to convert
each word in the string to pig latin.
Args:
userStr: A user given string
Returns:
A pig latin translated string pigStr
"""


def pigLatin(userStr):
    pigStr = ""
    wordList = userStr.split(" ")
    for word in wordList:
        pigWord = translate(word)
        pigStr = pigStr + pigWord + " "
    return pigStr


"""
Translates an individual word to pig latin based off pig latin
conventions.
Args:
word: An individual string in the lists of words of the user given
string.
Returns:
A pig latin translated word "word"
"""


def translate(word):
    # If hyphen is in word, split word and recurse for each word
    if "-" in word:
        i = 0
        hyphenWordList = word.split("-")
        pigWord = translate(hyphenWordList[i])
        while(i < (len(hyphenWordList) - 1)):
            i += 1
            pigWord = pigWord + "-" + translate(hyphenWordList[i])
        return pigWord

    j = 0
    puncIndex = []
    upperIndex = []
    puncList = []

    # Detects uppercase and punctuation
    # Stores index of uppercase character
    # Stores index of punctuation relative to end of word
    for char in word:
        if word[j].isupper():
            upperIndex.append(j)
        if word[j] in string.punctuation:
            puncIndex.append(len(word[j:])-1)
            puncList.append(word[j])
            puncRemoved = word[:j] + word[j+1:]
        j += 1
    # Sets word to punctuation removed version if needed
    if len(puncIndex) >= 1:
        word = puncRemoved

    # Basic cases
    if len(word) < 1:
        return ""
    if len(word) == 1:
        return word

    if word[len(word)-3:].lower() == "way":
        return word

    if word[0].lower() in vowels:
        word = word.lower() + "way"
    else:
        word = word[1:].lower() + word[:1].lower() + "ay"

    # Iterates through list, makes element uppercase if needed
    k = 0
    charList = list(word)
    while k < len(upperIndex):
        charList[upperIndex[k]] = charList[upperIndex[k]].upper()
        k += 1
    word = ''.join(charList)

    # Adds punctuation back in, relative to offset
    l = 0
    for punc in puncList:
        offset = len(word) - puncIndex[l]
        word = word[:offset] + puncList[l] + word[offset:]

    return word

userStr = input("Enter string: ")
print(pigLatin(userStr))
