'''
Daniel Edwards
10/22/2015
PigLatin.py
A program that translates a string into "pig-latin".
'''
import string #imported for string.punctuation

kVowels = ['a', 'e', 'i', 'o', 'u']

'''
This function takes a string as input and converts it to pig latin.
This function handles the hyphen case and calls the translate function.
@param aStr The string to be converted
@return Returns the converted string.
'''
def pigLatin(aStr):
    tStr = ""
    tWords = aStr.split(" ")
    for tWord in tWords:
        #check for hyphen
        if("-" in tWord):
            tHyphenList = tWord.split("-")
            tHyphen = ""
            #account for multiple hyphen case.
            for tHyphenWord in tHyphenList:
                tHyphen = tHyphen + translate(tHyphenWord) + "-"
            tWord = tHyphen[:len(tHyphen) - 1] #remove excess hyphen
        else:
            tWord = translate(tWord)
        tStr = tStr + tWord + " "
    return tStr

'''
This function translates a word to pig latin. It handles checking for vowels,
capitalization, punctuation and any edge cases that could cause problems.
@param aStr The word to be translated
@return Returns the translated word.
'''
def translate(aStr):
    if(len(aStr) < 1):
        return ""
    if(len(aStr) == 1):
        return aStr
    tIndex = 0
    tCapIndex = []
    tPuncIndex = {}
    
    for tChar in aStr:
        #check for upper case
        if(tChar.isupper()):
            tCapIndex.append(tIndex)
        #check for punctuation, remove and store location
        if(tChar in string.punctuation):
            aStr = aStr[:tIndex] + aStr[tIndex + 1:]
            tKey = (tIndex - len(aStr)) * -1
            tPuncIndex[tKey] = tChar
            tIndex = tIndex - 1
        tIndex = tIndex + 1

    #check if ends in way    
    if(aStr[len(aStr)-3:].lower() == "way"):
        return aStr

    aStr = aStr.lower()
    #check first letter and add way/ay
    if(aStr[0] in kVowels):
        aStr = aStr + "way"
    else:
        aStr = aStr[1:] + aStr[:1] + "ay"

    #adjust capitals    
    tCharList = list(aStr)
    for tCap in tCapIndex:
        tCharList[tCap] = tCharList[tCap].upper()
    aStr = ''.join(tCharList)
    
    #add punctuation back
    for tPunct in tPuncIndex.keys():
        tLoc = len(aStr) - tPunct
        aStr = aStr[:tLoc] + tPuncIndex[tKey] + aStr[tLoc:] 
    return aStr

#Calls the function, takes console input.
tStr = input("Enter your string: ")
tStr = pigLatin(tStr)
print tStr
