import os
import random
import sys
__author__ = 'joanhong'


def generate_essay(num_parag, num_sent, adjs, nouns, verbs):
    num_adjs = len(adjs)
    num_nouns = len(nouns)
    num_verbs = len(verbs)

    for np in range(num_parag):
        for ns in range(num_sent):

            count_nouns = random.randrange(num_nouns)
            count_verbs = random.randrange(num_verbs)

            clause_type = random.randrange(1)
            end = num_adjs/num_parag/num_sent
            if end == 0:
                end = 1
            adj_type1 = random.randrange(end)
            adj_type2 = random.randrange(end)

            sentence = ""
            for ind in range(adj_type1):
                count_adjs = random.randrange(num_adjs)
                sentence += adjs[count_adjs] + " "

            order = random.randrange(1)
            if clause_type == 0:
                if order == 0:
                    sentence += nouns[count_nouns] + " " + verbs[count_verbs]
                else:
                    sentence += verbs[count_verbs] + " " + nouns[count_nouns]

            if clause_type == 1:
                for ind in range(adj_type2):
                    sentence += adjs[count_adjs]
                count_nouns = random.randrange(num_nouns)
                sentence += nouns[count_nouns]
            sys.stdout.write(str.capitalize(sentence) + ". ")
        print "\n"


def check_valid_input(user_input):
    if not str.isdigit(user_input):
        print "Please enter a valid number"
        return False
    elif int(user_input) < 1:
        print "Please enter a valid number"
        return False
    else:
        return True


if __name__=="__main__":
    adjs_file = open(os.getcwd()+'/EssayMonkeyAdjectives.txt', 'r')
    nouns_file = open(os.getcwd()+'/EssayMonkeyNouns.txt', 'r')
    verbs_file = open(os.getcwd()+'/EssayMonkeyVerbs.txt', 'r')

    adjs_str = adjs_file.read()
    nouns_str = nouns_file.read()
    verbs_str = verbs_file.read()

    adjs_str.replace('\t', ' ')
    nouns_str.replace('\t', ' ')
    verbs_str.replace('\t', ' ')

    adjs_str.replace('/', ' ')
    nouns_str.replace('/', ' ')
    verbs_str.replace('/', ' ')

    adjs_in = adjs_str.split(',')
    nouns_in = nouns_str.split(',')
    verbs_in = verbs_str.split(',')

    running = True
    while running:
        num_parag_input = raw_input("Number of paragraphs: ")
        if check_valid_input(num_parag_input):
            num_sent_input = raw_input("Number of sentences per paragraph: ")
            if check_valid_input(num_sent_input):
                generate_essay(int(num_parag_input), int(num_sent_input), adjs_in, nouns_in, verbs_in)
                running = False