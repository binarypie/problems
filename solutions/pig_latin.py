#!/usr/bin/env python3
import sys


def pig_word(input_str):
    """Takes a single word and translates it to pig-latin"""
    if '-' in input_str:
        words = input_str.split('-')
        pig_words = [pig_word(word) for word in words]
        return '-'.join(pig_words)

    if len(input_str) == 1:
        return input_str

    upper_indexes = [index for index, letter in enumerate(input_str) if letter.isupper()]
    lower_input = input_str.lower()

    if lower_input.endswith("way"):
        return input_str

    if lower_input[:1] not in ['a', 'e', 'i', 'o', 'u']:
        result = "{}{}ay".format(lower_input[1:], lower_input[0])
    else:
        result = lower_input + "way"

    punctuation = [punc for punc in ['\'', '.', '!', '?', ':', ';', '/', '%'] if punc in result]
    for punc in punctuation:
        i = result.index(punc)
        pre_string = result[:i]
        post_string = result[(i+1):]
        result = "{}{}{}{}".format(pre_string, post_string[:3], punc, post_string[3:])

    result_list = list(result)
    for i in upper_indexes:
        result_list[i] = result_list[i].upper()

    return ''.join(result_list)


def pig_latin(input_str):
    """Takes a single string as input and translates it to pig-latin."""
    if not input_str:
        return input_str

    words = input_str.split(' ')
    pig_words = [pig_word(word) for word in words]
    translated = ' '.join(pig_words)

    return translated


def main(first_string):
    result = pig_latin(first_string)
    print(result)


if __name__ == '__main__':
    main(sys.argv[1])
