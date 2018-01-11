import sys
import random
import re

adjfile = "EssayMonkeyAdjectives.txt"
nounfile = "EssayMonkeyNouns.txt"
verbfile = "EssayMonkeyVerbs.txt"

# Determiners and conjunctions make for more understandable sentences
determiners = ['the','my','your','his','her','its','our','their','whose','this','that','these','those','which']
conjunctions = ['for','and','nor','but','or','yet','so']

# Each file is split and the words are store
adjectives = re.split(',|, ',open(adjfile).read().strip()[:-1])
nouns = re.split(',|, ',open(nounfile).read().strip()[:-1])
verbs = re.split(',|, ',open(verbfile).read().strip()[:-1])

# Pizzazz
punctuation = ['. ','? ','! ']

# Input can be command line arguments or entered afterwards
try:
    paragraphs = int(sys.argv[1])
    sentences = int(sys.argv[2])
except IndexError:
    paragraphs = int(raw_input())
    sentences = int(raw_input())

# Returns a list of the form: [determiner, adjective, (adjective), noun, verb]
def generate_sentence():
    sentence = []
    sentence.append(random.choice(determiners))

    # Chance to have two adjectives in front of a noun
    adjective_sets = {
            0 : random.choice(adjectives),
            1 : random.choice(adjectives) + ", " + random.choice(adjectives),
    }
    sentence.append(adjective_sets[random.randint(0,1)])

    sentence.append(random.choice(nouns))
    sentence.append(random.choice(verbs))
    return sentence

# Loops over the amount of paragraphs and the sentences per paragraph
for i in range(paragraphs):
    paragraph = ''
    for j in range(sentences):
        sentence = generate_sentence()
        sentence[0] = sentence[0].title() # Capitalize the first letter

        # Chance to use a conjunction to combine two sentences
        if random.randint(0,1) == 1:
            sentence.append(random.choice(conjunctions))
            sentence += generate_sentence()

        paragraph += ' '.join(sentence) + random.choice(punctuation)
    print paragraph + '\n'

