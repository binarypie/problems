'''
Daniel Edwards
10/27/2015
EssayMonkey.py
A program that generates an essay based on input number of paragraphs
and sentences per paragraph.

This program assumes text files are in the folder matching the expected
naming convention.
'''
import random #imported for randomizing sentence length

'''
This function takes number of paragraphs and sentences per paragraph as
input and generates an essay matching those characteristics based on
text files containing a list of nouns, verbs and adjectives.
@param aParagraphs number of paragraphs
@param aSentences number of sentences per paragraph
@return Returns the string containing the completed essay.
'''
def essayMonkey(aParagraphs, aSentences):
    tPCount = 0
    tStr = ""
    #generate lists
    tWordList = createWordLists()
    tNouns = tWordList[0]
    tVerbs = tWordList[1]
    tAdjec = tWordList[2]

    #loop until desired number of paragraphs complete
    while tPCount < aParagraphs:
        tStr = tStr + "    " #indent
        tSCount = 0

        #loop until desired number of sentences generated
        while tSCount < aSentences:
            tStr = tStr + generateSentence(tNouns, tVerbs, tAdjec)
            tSCount = tSCount + 1
        tStr = tStr + "\n \n" #add empty line between paragraphs
        tPCount = tPCount + 1
    return tStr

'''
This function opens and closes the files containing the nouns, verbs and
adjectives.
@return Returns a list containing each list of words.
'''
def createWordLists():
    tNounFile = open("EssayMonkeyNouns.txt", "r")
    tVerbFile = open("EssayMonkeyVerbs.txt", "r")
    tAdjecFile = open("EssayMonkeyAdjectives.txt", "r")
    tWordList = []

    tWordList.append(tNounFile.read().strip("\n").split(","))
    tWordList.append(tVerbFile.read().strip("\n").split(","))
    tWordList.append(tAdjecFile.read().strip("\n").split(","))

    tNounFile.close()
    tVerbFile.close()
    tAdjecFile.close()
    
    return tWordList

'''
This function generates a sentence from the lists of words given
as parameters. It tests randomly generated numbers to determine
how to structure each sentence.
@param aNouns the list of nouns
@param aVerbs the list of verbs
@param aAdjec the list of adjectives
@return Returns the sentence generated
'''
def generateSentence(aNouns, aVerbs, aAdjec):
    tStr = ""
    tRand = random.random()
    
    #repeat adding adjectives a semi-random number of times
    while tRand < 0.6:
        tStr = tStr + random.choice(aAdjec) + " "
        tRand = random.random()
        
    tStr = tStr + random.choice(aNouns) + " "
    tStr = tStr + random.choice(aVerbs) + " "

    #add second noun and additional adjectives semi-randomly
    if(tRand > 0.2):
        while tRand < 0.6:
            tStr = tStr + random.choice(aAdjec) + " "
            tRand = random.random()
        tStr = tStr + random.choice(aNouns)
    #capitalize first letter
    tStrList = list(tStr)
    tStrList[0] = tStrList[0].upper()
    tStr = ''.join(tStrList)
    return tStr + ". "

#take input and print the returned essay string.    
tParagraphs = input("Enter number of paragraphs: ")
tSentences = input("Enter number of sentences per paragraph: ")
tStr = essayMonkey(tParagraphs, tSentences)
print(tStr)
