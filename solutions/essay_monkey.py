#!/usr/bin/env python3
import sys
from random import randrange
from random import sample


class FileWordReader:
    def read_words(self, filename):
        with open(filename, 'r') as f:
            lines = f.read().splitlines()

        words = set()
        for line in lines:
            line_words = line.split(',')
            words.update(line_words)

        return words


class EssayMonkey:
    """A class that writes essays of variable sentence and paragraph count. Pool of words comes
        from external files"""
    def __init__(self, paragraph_count, sentence_count, *files, word_reader=FileWordReader()):
        if not isinstance(paragraph_count, int):
            raise ValueError("paragraph_count input '{}' is not an integer".format(paragraph_count))

        if not isinstance(sentence_count, int):
            raise ValueError("sentence_count input '{}' is not an integer".format(sentence_count))

        if len(files) < 1:
            raise ValueError("No word files were provided")

        self._paragraph_count = paragraph_count
        self._sentence_count = sentence_count

        words = set()
        for file in files:
            words.update(word_reader.read_words(file))

        self._words = words

    def write_essay(self):
        """Produces an essay based on the current paragraph and sentence counts, using the words
            provided when the object was created"""
        words_range = len(self._words) + 1

        paragraphs = []
        for _ in range(self._paragraph_count):
            sentences = []
            for _ in range(self._sentence_count):
                sentence_length = randrange(4, 33)
                words = [sample(self._words, 1)[0] for _ in range(sentence_length)]
                sentence = ' '.join(words)
                sentences.append(sentence)

            paragraph = "{}{}".format(". ".join(sentences), '.')
            paragraphs.append(paragraph)

        essay = "{}{}".format("\t", "\n\t".join(paragraphs))

        return essay

    def set_paragraph_count(self, paragraph_count):
        self._paragraph_count = paragraph_count

    def set_sentence_count(self, sentence_count):
        self._sentence_count = sentence_count


def main(paragraph_count, sentence_count, *files):
    monkey = EssayMonkey(paragraph_count, sentence_count, *files)
    result = monkey.write_essay()
    print(result)


if __name__ == '__main__':
    file_names = sys.argv[3:len(sys.argv) + 1]
    file_name_tuple = tuple(file_names)
    main(int(sys.argv[1]), int(sys.argv[2]), *file_name_tuple)
