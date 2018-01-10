import sys
import re

intext = sys.stdin.readline().split()
outtext = []
vowels = ['a','e','i','o','u']

# Converts a word to Pig Latin
def to_pig_latin(word):
    letters = [x for x in word if x.isalpha()]
    # If our word is a single letter, append it and continue
    if len(word) <= 1:
        return word

    # Move the first consonant letter to the end and append ay
    if letters[0].lower() not in vowels:
        letters.append(letters.pop(0))
        letters = letters + ['a', 'y']

    # Retain the first vowel letter and append way
    else:
        letters = letters + ['w', 'a', 'y']

    # Loop back through word and insert punctuation
    for i,letter in enumerate(word):
        if not letter.isalpha():
            # If our punctuation is at the end, append it
            if i == len(word) - 1:
                letters.append(letter)
            # Otherwise, get its distance from the right and insert it
            else:
                letters.insert(i - (len(word) - 1), letter)

            # The problem doesn't specify case of letters in punctuation spaces, so I make them lowercase
            letters[i] = letters[i].lower()
        # Ensure that capitalization remains in the same place
        elif letter.isupper():
            letters[i] = letters[i].upper()
        else:
            letters[i] = letters[i].lower()
    return ''.join(letters)

for word in intext:
    # If a word pair has a hyphen (or multiple) we must translate each word separately, but combine them with a hyphen
    if '-' in word:
        outtext.append('')
        for split_word in word.split('-'):
            outtext[-1] += (to_pig_latin(split_word) + '-')
        outtext[-1] = outtext[-1][:len(outtext[-1])-1] # Remove trailing hyphen
    # Otherwise, simply translate the word
    else:
        outtext.append(to_pig_latin(word))

print ' '.join(outtext)
