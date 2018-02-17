import re

english_text = "In a hole in the ground there lived a hobbit."
vowels = ('a', 'e', 'i', 'o', 'u')


def convert_hyphenated_word(word):
    words = word.split('-')
    return f"{convert_word(words[0])}-{convert_word(words[1])}"


def convert_word(word):
    if len(word) <= 1 or (len(word) >= 3 and word[-3:] == 'way'):
        return word
    elif word[0].lower() in vowels:
        return word + 'way'
    else:
        return f"{word[1:]}{word[0]}ay"


def generate_pig_latin_sentence(words, ending):
    pig_latin_words = []
    for w in words:
        if '-' in w:
            pig_latin_words.append(' ' + convert_hyphenated_word(w))
        elif w:
            pig_latin_words.append(' ' + convert_word(w))

    pig_latin_words.append(ending)
    return ''.join(pig_latin_words)


def generate_pig_latin(sentences):
    pig_latin_sentences = []
    for s in sentences:
        # Get the ending punctuation of the sentence
        ending = s[len(s) - 1]
        words = re.split(r"[\s\.\,\!\?]", s)
        pig_latin_sentences.append(generate_pig_latin_sentence(words, ending))
    return ''.join(pig_latin_sentences)


if __name__ == '__main__':
    # Use regex module to split text into sentences
    text = re.findall(r"[A-Za-z][^\.\,!?]*[\.\,!?]", english_text)
    # Remove first space
    print(generate_pig_latin(text)[1:])
