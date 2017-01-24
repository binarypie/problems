import sys, random
import re

def generate_sentence(adjectives, nouns, verbs, length):
    tokens = []
    for i in range(0, length):
        token_type = i % 3
        if token_type == 0:
            adjective = adjectives[random.randint(0, len(adjectives) - 1)]
            if i == 0:
                adjective = adjective.title()
            tokens.append(adjective)
        elif token_type == 1:
            tokens.append(nouns[random.randint(0, len(nouns) - 1)])
        elif token_type == 2:
            tokens.append(verbs[random.randint(0, len(verbs) - 1)])
    return " ".join(tokens) + "."

def generate_paragraph(adjectives, nouns, verbs, paragraph_len):
    sentences = []
    sentence_lengths = [n*3 for n in range(1, paragraph_len + 1)]
    random.shuffle(sentence_lengths)
    for i in range(0, paragraph_len):
        sentence_len = sentence_lengths[i]
        sentences.append(generate_sentence(adjectives, nouns, verbs, sentence_len))
    return " ".join(sentences)

def generate_essay(adjectives, nouns, verbs, num_paragraphs, paragraph_len):
    paragraphs = []
    for i in range(0, num_paragraphs):
        paragraphs.append(generate_paragraph(adjectives, nouns, verbs, paragraph_len))
    return "\n\n".join(paragraphs)

if __name__ == "__main__":
    adjective_filename = sys.argv[1]
    noun_filename = sys.argv[2]
    verb_filename = sys.argv[3]
    num_paragraphs = int(sys.argv[4])
    paragraph_len = int(sys.argv[5])
    with open(adjective_filename) as adjective_file, open(noun_filename) as noun_file, open(verb_filename) as verb_file:
        adjectives = re.split("[\W,]+", adjective_file.read())
        nouns = re.split("[\W,]+", noun_file.read())
        verbs = re.split("[\W,]+", verb_file.read())
        print(generate_essay(adjectives, nouns, verbs, num_paragraphs, paragraph_len))
