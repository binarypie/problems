import sys
import random


'''
Source: git@github.com:newbootz/problems.git
Website: https://github.com/newbootz/problems
Author: Jesus Galvan (@newbootz)

# Essay Monkey #

Given a set of txt files generate an essay.

* The function should take the number of paragraphs to generate.
* The function should take the number of sentences per peragraph to generate.
* Each sentence should be of any reasonable length but each should not be the same length.

## Input ##
python essay_monkey <number_of_paragraphs> <number_of_sentences_per_paragraph>

# Example Input #
python essay_monkey.py 5 12

'''


# Load verb, noun, and adjective files
a_file = "EssayMonkeyAdjectives.txt"
n_file = "EssayMonkeyNouns.txt"
v_file = "EssayMonkeyVerbs.txt"

# Open the word banks and generate iterable/indexable lists (verbs, adjectives, nouns) and return them
def provide_word_banks():
	verbs = []
	adjectives = []
	nouns = []

	with open(v_file, "r") as vf,open(n_file, "r") as nf, open(a_file, "r") as af:
		for line in vf:
			verbs = line.split(",")
			verbs = [v.strip() for v in verbs]
		for line in nf:
			nouns = line.split(",")
			nouns = [n.strip() for n in nouns]
		for line in af:
			adjectives = line.split(",")
			adjectives = [a.strip() for a in adjectives]

	return verbs, adjectives, nouns


# Generate a sentence given verbs, adj, and noun lists
# Sentence structure: ARTICLE {a, the} ADJECTIVE NOUN VERB ARTICLE ADJECTIVE NOUN.
def generate_sentence(verbs, adjectives, nouns):
	articles = ["a", "the"]
	upper_articles = ["A", "The"]
	sentence = []
	
	sentence.append(upper_articles[random.randint(0, 1)])
	sentence.append(nouns[random.randint(0, len(nouns)-1)])
	sentence.append(verbs[random.randint(0,len(verbs)-1)])
	sentence.append(articles[random.randint(0,1)])
	sentence.append(adjectives[random.randint(0, len(adjectives)-1)])
	sentence.append(nouns[random.randint(0, len(nouns)-1)]+".")

	return sentence

# Write an essay with given number of paragraphs and sentences per paragraph
def write_essay(number_of_p, sentences_per_p):
	essay = []
	verbs, adjectives, nouns = provide_word_banks()
	for p in range(0,int(number_of_p)):
		paragraph = []
		for s in range(0,int(sentences_per_p)):
			sentence = generate_sentence(verbs, adjectives, nouns)
			paragraph.append(" ".join(sentence))
		essay.append("\t"+" ".join(paragraph)+"\n\n")
	return "".join(essay)



def main(number_of_p, sentences_per_p):
	print write_essay(number_of_p, sentences_per_p)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])