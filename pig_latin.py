import sys

VOWELS = ["a", "e", "i", "o", "u"]
PUNCTUATION = [",", ".", "'", '"', ":", ";", "!", "?", "(", ")"]

def translate(str):
    def translate_word(word):
        original_len = len(word)
        if original_len == 1:
            return word
        elif "-" in word:
            return "-".join(map(translate_word, word.split("-")))
        elif word[-3:].lower() == "way":
            return word #don't modify words already ending in "way"

        #list of capitalizations of each character, ex: [True, False, False] for "Aaa"
        caps = map(lambda char: True if char.isupper() else False, word)
        #list of the form (i, punc_char) where punc_char is a punctuation character and i is
        #its location in the word
        punc_chars = reduce(
            lambda acc, pair: acc + [pair] if pair[1] in PUNCTUATION else acc,
            enumerate(word),
            [])
        #strip all punctuation characters from the word
        word = reduce(lambda new_word, char: new_word if char in PUNCTUATION else new_word + char, word, "")

        if word[0].lower() in VOWELS:
            word = word + "way" #vowel rule
        else:
            word = word[1:] + word[0] + "ay" #consonant rule

        #recapitalize word according to capitalization rule
        for i in range(0, original_len):
            word = word[:i] + (word[i].upper() if caps[i] else word[i].lower()) + word[i+1:]
        #re-insert punctuation
        for pair in punc_chars:
            punc_index = pair[0] - original_len #index of punctuation relative to end of word
            if punc_index == -1:
                word = word + pair[1]
            else:
                punc_index += 1
                word = word[:punc_index] + pair[1] + word[punc_index:]
        return word
    words = str.split(" ")
    words = map(translate_word, words)
    return " ".join(words)

if __name__ == "__main__":
    input_filename = sys.argv
    with open(input_filename) as file:
        for line in file:
            print(translate(line))
