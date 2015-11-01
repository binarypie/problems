import os
import random
import sys
__author__ = 'joanhong'


# generate essay based on input number of paragraphs and sentences
def generate_essay(num_parag, num_sent):

    adjs = parse_text_files("EssayMonkeyAdjectives.txt")
    nouns = parse_text_files("EssayMonkeyNouns.txt")
    verbs = parse_text_files("EssayMonkeyVerbs.txt")

    num_adjs = len(adjs)
    num_nouns = len(nouns)
    num_verbs = len(verbs)

    # determine how many adjectives per noun
    target = num_adjs/num_parag/num_sent
    # keep it to a reasonable range
    if target == 0:
        target = 1
    elif target > 7:
        target = 7

    punctuation = ['.', '!', '?']

    for np in range(num_parag):
        for ns in range(num_sent):
            # track array location
            adjs_loc = random.randrange(num_adjs)
            nouns_loc = random.randrange(num_nouns)
            verbs_loc = random.randrange(num_verbs)

            # randomize number of adjectives for each noun
            adj_type1 = random.randrange(target+1)
            adj_type2 = random.randrange(target+1)

            # construct the sentence
            sentence = ""

            # randomize clause type: noun-verb, verb-noun, noun-verb-noun
            clause_type = random.randrange(2)
            if clause_type == 0:
                order = random.randrange(2)
                # adj-noun-verb
                sentence += generate_adjectives(adj_type1, adjs_loc, adjs)
                sentence += nouns[nouns_loc] + " " + verbs[verbs_loc]

                # adj-noun-verb-adj-noun
                if order == 0:
                    adjs_loc = random.randrange(num_adjs)
                    sentence += " " + generate_adjectives(adj_type2, adjs_loc, adjs)
                    nouns_loc = random.randrange(num_nouns)
                    sentence += nouns[nouns_loc]
            else:
                # verb-adj-noun
                sentence += verbs[verbs_loc] + " "
                sentence += generate_adjectives(adj_type1, adjs_loc, adjs)
                sentence += nouns[nouns_loc]
            sys.stdout.write(str.capitalize(sentence) + punctuation[random.randrange(3)] + " ")
        sys.stdout.write("\n\n")


# generate target_adjs long adjective string using adjs array
def generate_adjectives(target_adjs, adjs_loc, adjs):
    sentence = ""
    num_adjs = len(adjs)
    for ind in range(target_adjs):
        if adjs_loc < num_adjs:
            sentence += adjs[adjs_loc] + " "
            adjs_loc += random.randrange(1, 3)
        else:
            adjs_loc = 0
    return sentence


# parse the text file and return array of words
def parse_text_files(filename):
    # open file for reading only
    file = open(os.getcwd()+'/'+filename, 'r')
    word_str = file.read()

    # replace tabs and forward slashes
    word_str = word_str.replace('\t', '')
    word_str = word_str.replace('/', ',')

    # split into arrays
    words = word_str.split(',')

    # filter out entries with zero length
    words = filter(None, words)
    return words


# check if valid user input to command line
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
    running = True
    while running:
        num_parag_input = raw_input("Number of paragraphs: ")
        if check_valid_input(num_parag_input):
            num_sent_input = raw_input("Number of sentences per paragraph: ")
            if check_valid_input(num_sent_input):
                generate_essay(int(num_parag_input), int(num_sent_input))
                running = False