import sys
import random


# line needs to be 83 characters, end with \n
# sentence needs to be diff lengths
#paragraphs begin with \t
# need to ignore words with len of 1 \t \n and " " after we strip them


# Open and load verb, noun, and adjective files
a_file = "EssayMonkeyAdjectives.txt"
n_file = "EssayMonkeyNouns.txt"
v_file = "EssayMonkeyVerbs.txt"

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

def generate_sentence(verbs, adjectives, nouns):
	articles = ["a", "the"]
	upper_articles = ["A", "The"]
	sentence = []
	# Sentence structure: ARTICLE {a, the} ADJECTIVE NOUN VERB ARTICLE ADJECTIVE NOUN.
	sentence.append(upper_articles[random.randint(0, 1)])
	sentence.append(nouns[random.randint(0, len(nouns)-1)])
	sentence.append(verbs[random.randint(0,len(verbs)-1)])
	sentence.append(articles[random.randint(0,1)])
	sentence.append(adjectives[random.randint(0, len(adjectives)-1)])
	sentence.append(nouns[random.randint(0, len(nouns)-1)]+".")

	return sentence


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