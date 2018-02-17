"""
Krishna Chaitanya Kandula
"""

import random
import sys

nouns_txt_file_name = 'EssayMonkeyNouns.txt'
verbs_txt_file_name = 'EssayMonkeyVerbs.txt'
adjectives_txt_file_name = 'EssayMonkeyAdjectives.txt'


def generate_clause(nouns, verbs, adjectives):
    noun1 = nouns[random.randint(0, len(nouns) - 1)]
    noun2 = nouns[random.randint(0, len(nouns) - 1)]
    verb = verbs[random.randint(0, len(verbs) - 1)]
    adj = adjectives[random.randint(0, len(adjectives) - 1)]
    return f"{adj} {noun1} {verb} {noun2}"


def generate_paragraph(num_sentences, nouns, verbs, adjectives):
    sentences = []
    for _ in range(0, num_sentences):
        sentence = []
        num_clauses = random.randint(2, 4)
        for x in range(0, num_clauses):
            join = ', and ' if x < num_clauses - 1 else '. '
            sentence.append(f"{generate_clause(nouns, verbs, adjectives)} {join}")
        sentences.append(''.join(sentence))
    sentences.append('\n \n')
    return sentences


def generate_essay(num_paragraphs, num_sentences):
    nouns_file = open(nouns_txt_file_name, 'r')
    nouns = nouns_file.read().split(',')
    verbs_file = open(verbs_txt_file_name, 'r')
    verbs = verbs_file.read().split(',')
    adj_file = open(adjectives_txt_file_name, 'r')
    adjectives = adj_file.read().split(',')

    essay = []
    for _ in range(0, num_paragraphs):
        paragraph = generate_paragraph(num_sentences, nouns, verbs, adjectives)
        essay.append(''.join(paragraph))
    return ''.join(essay)


if __name__ == '__main__':
    # Check args format
    if len(sys.argv) != 3:
        raise Exception('invalid number of arguments')
    print(generate_essay(int(sys.argv[1]), int(sys.argv[2])))
