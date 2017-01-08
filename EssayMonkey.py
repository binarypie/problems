
# ****************************************************************************************************
# Module functionality: Provides solution for the Problem EssayMonkey to generate an essay.          *
# Author: Sai Priya Sudhi Reddy                                                                      *
# Version Number: 0.1                                                                                *
# Date of Creation:  1/06/2017                                                                       *                                                                                                  
# EssayMonkey Function:                                                                              *
# 1.It takes the number of paragraphs to generate.                                                   *
# 2.It takes the number of sentences per paragraph to generate.                                      *
# Prerequisite Files: The Files EssayMonkeyVerbs.txt,EssayMonkeyNouns.txt,EssayMonkeyAdjectives.txt  *
#                     Should be placed in the same location where Essaymonkey.py is placed           *
# ****************************************************************************************************
import random
fileNouns = open("EssayMonkeyNouns.txt")                        #fileNouns contains reference to EssayMonkeyNouns.txt file
fileAdjectives = open("EssayMonkeyVerbs.txt")                   #fileAdjectives contains reference to EssayMonkeyVerbs.txt file
fileVerbs = open("EssayMonkeyAdjectives.txt")                   #fileVerbs contains reference to EssayMonkeyAdjectives.txt file
dataNouns = fileNouns.read()
dataVerbs = fileVerbs.read()
dataAdjectives = fileAdjectives.read()
wordsNouns = dataNouns.split(",")                               #wordsNouns contains list of all words in the file EssayMonkeyNouns.txt
wordsVerbs = dataVerbs.split(",")                               #wordsVerbs contains list of all words in the file EssayMonkeyVerbs.txt
wordsAdjectives = dataAdjectives.split(",")                     #wordsAdjectives contains list of all words in the file EssayMonkeyAdjectives.txt
lentNouns = len(wordsNouns)
lentVerbs = len(wordsVerbs)
lentAdjectives = len(wordsAdjectives)


def EssayMonkey(NParas,NLines):
    NumberOfParas =0
    essay = ""
    while(NumberOfParas<NParas):
        NumOflines = 0
        paragraph = ""
        while(NumOflines < NLines):
            NumberOfWords = 0
            sentence = ""
            Nwords = random.randint(10,15)                  #I assumed that each sentence will have 10-15 words
            while(NumberOfWords <Nwords): 
                randnum = random.randint(1,3)
                if(randnum == 1) : 
                    sentence+= wordsNouns[random.randint(1,lentNouns-1)]
                elif(randnum == 2) : 
                    sentence+= wordsVerbs[random.randint(1,lentVerbs-1)]
                else: 
                    sentence+= wordsAdjectives[random.randint(1,lentAdjectives-1)]
                if(NumberOfWords != Nwords-1):
                    sentence +=" "
                NumberOfWords+=1  
            sentence+="."
            paragraph += sentence
            NumOflines+=1 
        paragraph+="\n" 
        paragraph+="\n"
        essay += paragraph
        NumberOfParas +=1  
    return essay


essay = EssayMonkey(5,3)
print essay


    



