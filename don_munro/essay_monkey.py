
"""
... 
This is a work in progress ... stashed here with hopes I'll get back to it ASAP.  
Outstanding part of this problem is identifying a couple/few different patterns that 
can be used to form sentences -- that vary in length to some degree.  

Sentence patterns : 

http://support.lexercise.com/hc/en-us/community/posts/220971647-Basic-English-Sentence-Patterns
http://grammar.ccc.commnet.edu/grammar/definitions.htm

"""

import sys
import random

ARTICLES = ['a', 'an', 'the']
INIT = ["A", 'The', ]
CONJUNCTIONS = ['and', 'or']


class EssayMonkey(object):

    def __init__(self):
        self.nouns = self._read_file("../EssayMonkeyAdjectives.txt")
        self.adjectives = self._read_file("../EssayMonkeyVerbs.txt")
        self.verbs = self._read_file("../EssayMonkeyNouns.txt")

    @staticmethod
    def _read_file(filename):
        with open(filename, 'r') as inputfile:
            full_text = inputfile.read()

        word_list = full_text.split(',')
        return word_list

    def get_random(self, word_list):
        idx = random.randint(0, len(word_list) - 1)
        return word_list[idx]

    def generate_sentence(self):
        # Notes:
        #  - sentences are to be reasonable length BUT ... not all the same length.
        #
        #  - solution needs to define one or more patterns for sentences that pull
        #    at random from the known nouns, adjectives and verbs.  To ensure proper
        #    sentence structure patterns may also make use of defined 'articles' and
        #    'conjunctions'
        return "This is a sentence...tbd. "


    def generate_essay(self, num_paragraphs, sentences_per_paragraph):

        essay = ''
        for para_count in range(num_paragraphs):
            paragraph = ''
            for sent_count in range(sentences_per_paragraph):
                paragraph = paragraph + self.generate_sentence()
            paragraph += "\r\n\n"
            essay += paragraph


        return essay



def main(argv):

    if len(argv) == 3:
        num_paragraphs = argv[1]
        num_sentences = argv[2]
    else:
        num_paragraphs = raw_input("Paragraphs: ")
        num_sentences = raw_input("Sentences: ")

    monkey = EssayMonkey()
    essay = monkey.generate_essay(num_paragraphs, num_sentences)
    print essay


if __name__ == "__main__":
    main(sys.argv)
