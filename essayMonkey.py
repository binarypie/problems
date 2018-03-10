'''
Kamran Madatov Electronic Arts

Essay Monkey Solution


Given a set of txt files generate an essay.
1. The function should take the number of paragraphs to generate.
2. The function should take the number of sentences per peragraph to generate.
3. Each sentence should be of any reasonable length but each should not be the same length.

See EssayMonkeyVerbs.txt
See EssayMonkeyNouns.txt
See EssayMonkeyAdjectives.txt


How to run:
Must have Python Idle Installed
Version: Python 3.6.3

1. Open terminal
2. Navigate to the file directory
3. Run on terminal: python3 essayMonkey.py
4. The terminal will ask you to input parameters, enter accordingly

'''

#modules
import sys
import random


#SIXTH STEP
#Parse through wordfile and return a random word
def getWord(wordFile):
    word = ''
    wordsList = wordFile.readline().split(',') #store words to a list
    lengthWords = len(wordsList) - 1           #extract length of words, without '\n' 
    wordsList.pop(lengthWords)                     #remove "\n" syntax
    randomWordNum = random.randint(0, lengthWords)
    if randomWordNum  < lengthWords:
        word = wordsList[randomWordNum]
    return word


#FIFTH STEP
#Extract file data
def getNoun():
    nounF = open('EssayMonkeyNouns.txt', 'r')
    return getWord(nounF)
    
def getVerb():
    verbF = open('EssayMonkeyVerbs.txt', 'r')
    return getWord(verbF)

def getAdjective():
    adjectivesF = open('EssayMonkeyAdjectives.txt', 'r')
    return getWord(adjectivesF)



    
#FOURTH STEP
#generate a sentence
def getSentence():
    #Maximum of words per sentence 
    numberWords = random.randint(1, 33)    #33 max words => n - 3 every iteration
    sentence = ''
    while numberWords > 0:
        sentence += getNoun() + ' ' + getVerb() + ' ' + getAdjective() + ' '
        numberWords -= 3
    sentence=' '.join(sentence.split())
    sentence = sentence[0].upper() + sentence[1:]
    sentence += '. '
    return sentence

#THIRD STEP
#generate a paragraph
def getParagraph(numbSente):
    indexLength = [ ]
    counter = 0
    paragraph = '' 
    while counter < numbSente:
        sentence = getSentence()
        lengthSen = len(sentence)
        if lengthSen not in indexLength and lengthSen > 2:  #Preven Length of sentences be equal per paragraph
            counter += 1
            paragraph = (paragraph + sentence)
            indexLength.append(lengthSen)
    paragraph += '\n'
    return paragraph

       
#SECOND STEP
#generate Paragraphs
def getEssay(numbPara, numbSente):
    paraCounter = numbPara
    paragraphs = ''
    while paraCounter > 0:
        paragraphs += getParagraph(numbSente)
        paraCounter -= 1
    return paragraphs

#FIRST STEP    
#Ask the user for the essay parameters
def main():
    print ("Welcome to the Essay Monkey Generator")
    try:
        numParas = int(input('Enter number of paragraphs: '))
        numSentes =  int(input('Enter number of sentences: '))
    except:
        print("That's not an int!")
    essay=getEssay(numParas, numSentes)
    print (essay)

#STEP ZERO
#Run main 
if __name__ == "__main__":
    main()

