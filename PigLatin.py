import string

def pig_latin (str):
    word_list = split_delim(str, [" ", "-"])
    pig_list = []
    for pair in word_list:
        word, delim = pair
        if len(word) <= 1 or word.endswith("way"):
            pig_list.append((word, delim))
            continue
        word_np, punct_list = save_punct(word)
        if vowel_start(word_np):
            word_np = word_np + "way"
        else:
            word_np = word_np[1:] + word_np[0] + "ay"
        if len(punct_list) > 0:
            pig_latin = join_punct(word_np, punct_list)
        else:
            pig_latin = word_np
        pig_list.append((pig_latin, delim))
    print(join_delim(pig_list))

def join_punct(str, punct_list):
    print(punct_list)
    for i, punct_pair in enumerate(punct_list):
        index, punct = punct_pair
        #End index is length minus the index, plus the amount of
        #further punctuation that needs to be added
        end_index = len(str) - index + (len(punct_list) - 1 - i)
        str = str[0:end_index] + punct + str[end_index:]
    return str

def save_punct(str):
    punct_list = []
    word = ""
    for index, char in enumerate(str):
        if char in string.punctuation:
            punct_list.append((len(str) - 1 - index, char))
        else:
            word += char
    return (word, punct_list)

def join_delim(list):
    str = ""
    for pair in list:
        word, delim = pair
        str += word + delim
    return str


def split_delim(str, delim):
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
    VOWELS = ["a", "e", "i", "o", "u"]
    return str[0].lower() in VOWELS

test_example = "HeLLo World! I can't. wait to coway explore your VAST forests. The-End!"
pig_latin(test_example)
