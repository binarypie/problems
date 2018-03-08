
import random
import sys

NOUNS = "EssayMonkeyNouns.txt"
VERBS = "EssayMonkeyVerbs.txt"
ADJECT = "EssayMonkeyAdjectives.txt"

# (adj) NOUN VERB (adj*) (noun) /and sentence
class Essay:
    def __init__(self):
        self.noun_list = self.read_file(NOUNS)
        self.verb_list = self.read_file(VERBS)
        self.adj_list = self.read_file(ADJECT)

    def generate_essay(self, para, sent):
        """Returns string length based on paragraph
        and sentence length.

        para -- number of paragraphs
        sent -- number of sentences
        """
        essay = ""
        for i in range(para):
            para = ""
            for j in range(sent):
                para += self.generate_sentence() + " "
            essay += para + "\n\n"
        return essay[0:len(essay)-2]

    def generate_sentence(self, compound=False):
        """Returns a sentence based on parts of speech
        from text files.

        Sentence is defined in this function by atleast
        a NOUN + VERB, with a chance of NOUN VERB NOUN
        and a chance of adjectives before NOUN's and
        compound sentence.

        compound -- if true sentence cannot be compound
        """
        sent = ""
        if random.randint(1, 10) > 3:
            sent += self.adj() + " "
        sent += self.noun() + " "
        sent += self.verb() + " "
        if random.randint(1, 10) > 4:
            if random.randint(1, 10) > 3:
                sent += self.adj() + " "
            sent += self.noun()+ " "
        if compound:
            return sent
        if random.randint(1, 10) > 7:
            sent += "and " + self.generate_sentence(True)
        return sent[0].upper() + sent[1:len(sent)-1] + "."

    def adj(self):
        """Returns random str from adj_list"""
        return self.adj_list[random.randint(0, len(self.adj_list)-1)]

    def noun(self):
        """Returns random str from noun_list"""
        return self.noun_list[random.randint(0, len(self.noun_list)-1)]

    def verb(self):
        """Returns random str from verb_list"""
        return self.verb_list[random.randint(0, len(self.verb_list)-1)]

    def read_file(self, str):
        """Returns a list of strings from reading str"""
        f = open(str, "r")
        return f.read().strip().split(",")

if len(sys.argv) == 3:
    e = Essay()
    try:
        par = int(sys.argv[1])
        sent = int(sys.argv[2])
    except:
        sys.exit("Command line argument must be integers")
    print(e.generate_essay(par, sent))
else:
    sys.exit("Essaymonkey requires two integers")
