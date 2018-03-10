'''
Kamran Madatov Electronic Arts

Pig Latin Solution

Code that translates a string (word, sentence, or paragraph) into “pig-latin” using the following rules.
1. Words that start with a consonant have their first letter moved to the end of the word and the letters “ay” added to the end.
2. Words that start with a vowel have the letters “way” added to the end.
3. Words that end in “way” are not modified.
4. Punctuation must remain in the same relative place from the end of the word.
5. Hyphens are treated as two words
6. Capitalization must remain in the same place.
7. Single letters are not modified.

Example:
    input: "HeLLo World! I can't wait to explore your VAST forests. The-End!"
    output: "ElLOhay Orldway! I antca'y aitway otay exploreway ouryay ASTVay orestsfay. Hetay-Endway!"

How to run:
Must have Python Idle Installed
Version: Python 3.6.3

1. Open terminal
2. Navigate to the file directory
3. Run on terminal: python3 pigLatin.py
4. The terminal will ask you to input a string, enter what you may like
'''


#Import Modules
import sys
import string


#SIXTH STEP
#Insert punctuation with the given key(from the right) and punctuationKey-value pair
def punctuate(word, keyValuePunc):
    counter = 0
    for key, value in keyValuePunc.items():
        lengthAdjust = len(keyValuePunc) + len(word) + counter
        word = word[0: lengthAdjust - key] + value + word[lengthAdjust - key:]
        counter -= 1    #adjusts as len of word changes
    return word


#FIFTH STEP
#Letter case accordingly with the corresponding capitalized index of the original word
def letterCase (word, indexCapt):
    return ("".join(c.upper() if i in indexCapt else c.lower() for i, c in enumerate(word)))


#FOURTH STEP (consonant & vowel)
#Words that start with a consonant have their first letter moved to the end of the wordand the letters “ay” added to the end.
def consonant(consonantWord):
    if consonantWord[-3:].lower() == "way":
        return consonantWord
    else:
        return consonantWord[1:] + consonantWord[0] + 'ay'

#Words that start with a vowel have the letters “way” added to the end.
def vowel(vowelWord):
    if vowelWord[-3:].lower() == "way":
        return vowelWord
    else:
        return vowelWord + 'way'


#THIRD STEP
#ANALYZE Each word 
def analyzeWord(word):
    adjustIndex = 0
    keyValuePunc = {}
    indexCapt = []
       
    for index, letter in enumerate(word):  #strip and store punctuations and its corresponding index from the right for step six
        if letter in string.punctuation:
            lengthWord = len(word)
            indexFromRight = ((lengthWord + adjustIndex) - index)
            keyValuePunc[indexFromRight] = letter
            word = word[0: index - adjustIndex] + word[index + 1 - adjustIndex:]
            adjustIndex += 1


            
    for index,letter in enumerate(word):  #store index of the capitalized letters after punctuation is stripped for step five
        if letter.isupper():
            indexCapt.append(index)
            
    if len(word) == 0 or len(word) == 1: #after stripped of punctuators 
        return punctuate(word, keyValuePunc)       
    elif word[0] in "AEIOUaeiou": #if first letter is vowel, we will consider 'y' as a consonant as a design decision
        return punctuate(letterCase(vowel(word), indexCapt), keyValuePunc) #Run through vowel function, then letterCase, and punctuate
    else:                         #else first letter is consonant
        return punctuate(letterCase(consonant(word), indexCapt), keyValuePunc) #Run through consonant function, then letterCase, and punctuate
    

#SECOND STEP    
#Parse string and separate words 
def pigLatin (inputString):
    inputList = inputString.split()
    outputList = []
    for word in inputList:
            if len(word) == 1:     #Single letters are not modified.
                outputList.append(word)
            elif (any(str.isdigit(c) for c in word)): #not a word, don't apply any changes
                outputList.append(word)
            elif word[-3:].lower() == "way":          #ends with way, dont apply any changes
                outputList.append(word)
            elif '-' in word: #contains two words, ignoring text after second hypen within the string
                hyphenWords = word.split('-')
                outputList.append(analyzeWord(hyphenWords[0]) + '-' + analyzeWord(hyphenWords[1]))
            else:            
                outputList.append(analyzeWord(word)) #rest
    outputString = ' '.join(outputList)
    return outputString

#FIRST STEP    
#Ask the user what to translate
def main():
    print ("Welcome to the Pig-Latin Translator Program")
    inputString = input('Please enter the text you would like to be translated into pigLatin: ')
    translatedString = pigLatin(inputString)
    print ("Pig-Latin Translation")
    print (translatedString)
    

#STEP ZERO
#Run main 
if __name__ == "__main__":
    main()
