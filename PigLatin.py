import string
import sys


def pig_latin (str):
    """Returns pig latin version of str, where str
    can be a word or multiple words.

    """
    word_list = split_delim(str, [" ", "-"])
    pig_list = []
    for pair in word_list:
        word, delim = pair
        word_np, punct_list = save_punct(word)
        if len(word_np) <= 1 or word_np.endswith("way"):
            pig_list.append((word, delim))
            continue
        if vowel_start(word_np):
            word_np = word_np + "way"
        else:
            word_np = word_np[1:] + word_np[0] + "ay"
        if len(punct_list) > 0:
            pig_latin = join_punct(word_np, punct_list)
        else:
            pig_latin = word_np
        pig_list.append((pig_latin, delim))
    return join_delim(pig_list)

def join_punct(str, punct_list):
    """Returns a string formed by placing each
    punct in punct_list back into str

    str - str to place punctuation
    punct - list of (index, punct_list) tuples
    """
    for i, punct_pair in enumerate(punct_list):
        index, punct = punct_pair
        #End index is length minus the index, plus the amount of
        #further punctuation that needs to be added
        end_index = len(str) - index + (len(punct_list) - 1 - i)
        str = str[0:end_index] + punct + str[end_index:]
    return str

def save_punct(str):
    """Returns a tuple, (word, punct_list),
    word -- input str with punctuation stripped out
    punct_list -- list of tuples, (index, punct) where
    index is the location of removed punct

    str -- the str to remove punctuation from
    """
    punct_list = []
    word = ""
    for index, char in enumerate(str):
        if char in string.punctuation:
            punct_list.append((len(str) - 1 - index, char))
        else:
            word += char
    return (word, punct_list)

def join_delim(list):
    """Returns a string formed by joining the first
    element and second element of each tuple in list

    list -- a list of tuple (str, delim) to be concatenated
    """
    str = ""
    for pair in list:
        word, delim = pair
        str += word + delim
    return str


def split_delim(str, delim):
    """Returns a list of tuples, (str, delim),
    of each str seperated by delim and the delim

    str -- the str to be seperated
    delim -- list of delims to seperate by
    """
    split_list = []
    word = ""
    for char in str:
        if char in delim:
            split_list.append((word, char))
            word = ""
        else:
            word += char
    split_list.append((word, ""))
    return split_list

def vowel_start(str):
    """Returns true if string starts with a vowel"""
    VOWELS = ["a", "e", "i", "o", "u"]
    return str[0].lower() in VOWELS

word = input("Input: ")
print(pig_latin(word))
