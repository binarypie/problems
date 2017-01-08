# -*- coding: utf-8 -*-
# ****************************************************************************************************                                                                              *
# Module functionality: Provides solution for the Problem Pig Latin that translates a string(word,   *
# sentence, or paragraph) into pig-latin using the rules                                             *
# Author: Sai Priya Sudhi Reddy                                                                      *
# Version Number: 0.1                                                                                *
# Date of Creation:  1/06/2017                                                                       *                                                               
# ****************************************************************************************************

import re

# ****************************************************************************************************
# getIndices Function:                                                                               *
# Input :                                                                                            *
#  String is passed as input to this function                                                        *  
# Output :                                                                                           *
#  It returns the indices of Upper Case Letters                                                      *
# ****************************************************************************************************

def getIndices(s):
    return [i for i, c in enumerate(s) if c.isupper()]

# ****************************************************************************************************
# getSplIndices Function:                                                                            *
# Input :                                                                                            *
#  String is passed as input to this function                                                        *  
# Output :                                                                                           *
#  It returns the dictionary of indices and special Character at that index                          *
# ****************************************************************************************************

def getSplIndices(s):
    lenword=len(s)
    d={}
    for i, c in enumerate(s) :
        if not(c.isupper() or c.islower() or c.isalnum()):
            d[i-lenword]=s[i-lenword]
    return d

# ****************************************************************************************************
# deleteSplChar Function                                                                             *
#  It deletes the Special Characters at original position to place it in relative position later     *                                                                     *
# Input :                                                                                            *
#  String and Special Character Dictionary are passed                                                *  
# Output :                                                                                           *
#  It deletes the Special Characters at original position to place it in relative position later     *
# ****************************************************************************************************

def deleteSplChar(word,splChar):
    for key in sorted(splChar.iterkeys()):
        if key != -1 :
            word=word[-len(word):key]+word[key+1:]
        else:
            word=word[-len(word):key]
    return word

# ****************************************************************************************************
# addSplChar Function:                                                                               *
#  It adds the Special Characters to same relative position from the Last                            *
# Input :                                                                                            *
#  String and Special Character Dictionary are passed                                                *  
# Output :                                                                                           *
#  word is returned with Special Characters in same relative position from the Last                  *
# ****************************************************************************************************

def addSplChar(word,splChar) :
    for key in sorted(splChar.iterkeys(),reverse=True):
        if key != -1 :
            word=word[-len(word):key+1]+splChar[key]+word[key+1:]
        else:
            word=word[-len(word):]+splChar[key]
    return word

# ****************************************************************************************************
# upperLetConv Function:                                                                             *
# Capitalization remains in the same place.                                                       *
# Input :                                                                                            *
#  A word in String and upper case letters indices for that word are passed                          *  
# Output :                                                                                           *
#  Word is returned with Capital Letters in same position as Original                                *
# ****************************************************************************************************

def upperLetConv(word,upperLet):
    word=word.lower()
    word=list(word)
    for i in upperLet:
        word[i]=word[i].upper()
        #print word[i]
    word=''.join(word)
    return word

# ****************************************************************************************************
# PigLatin Function:                                                                                 *
# It takes string as input and translates the sentence into pig-latin using the following rules      *
#  1. Words that start with a consonant have their first letter moved to the end of the word and the *
#     letters �ay� added to the end.                                                                 *
#  2. Words that start with a vowel have the letters �way� added to the end.                         *
#  3. Words that end in �way� are not modified.                                                      *
#  4. Punctuation must remain in the same relative place from the end of the word.                   *
#  5. Hyphens are treated as two words                                                               *
#  6. Capitalization must remain in the same place.                                                  *
#  7. Single letters are not modified.                                                               *
# ****************************************************************************************************

def pigLatin():
    text=input('Enter the string :')
    print text
    textList=re.split(r'([ -])',text)
    finalList=[]
    for word in textList:
        if word.endswith('way') or len(word)==1 or word==' ' or word=='-':
            finalList.append(word)
        elif word[0] in 'aeiouAEIOU':
            splChar=getSplIndices(word)
            word=deleteSplChar(word,splChar)
            word= word + "way"
            word=addSplChar(word,splChar)
            finalList.append(word)
        else : 
            upperLet=getIndices(word)
            splChar=getSplIndices(word)
            word=deleteSplChar(word,splChar)
            word=word[1:len(word)+1]+word[0]+"ay"
            word=upperLetConv(word,upperLet)
            word=addSplChar(word,splChar)
            finalList.append(word)
    finalStr=''.join(finalList)
    print finalStr

    
pigLatin()
