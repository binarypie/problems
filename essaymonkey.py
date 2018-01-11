import sys
import random
import re

def loadfile(filename):
    """
    Read files from the same directory
    """
    line = ""
    with open(filename) as f:
        line = f.readline().strip()
    return line.split(",")

def processwordlist(wordlist):
    """
    Processes the list of words to remove special characters i.e. () and /
    """
    output = []
    for word in wordlist:
        word = word.strip()
        # Split into separate words
        if "/" in word:
            words = word.split("/")
            for w in words:
                output.append(w.strip())
            continue
        # Remove other special characters
        s = re.sub('[^A-Za-z ]+', '', word)
        output.append(s)
    return output

def essaymonkey(paragraphs, sentences):
    adjectives = loadfile("EssayMonkeyAdjectives.txt")
    nouns = loadfile("EssayMonkeyNouns.txt")
    verbs = loadfile("EssayMonkeyVerbs.txt")

    # Assuming that the the specials characters "/" and "()" are in the words list
    # intentionally, they will be used in the essay as is. If they need to be removed,
    # they can be removed using the processwordlist()
    #adjectives = processwordlist(adjectives)
    #nouns = processwordlist(nouns)
    #verbs = processwordlist(verbs)

    output = "\t"
    for i in range(0, paragraphs):
        for j in range(0, sentences):
            length = random.randint(1, 5) # length of sentence between 3 to 15 words
            # The sentence will contain sets of 3 random adjective, noun, and verb
            for k in range(0, length):
                # Capitalize beginning of sentence
                if k == 0:
                    output += nouns[random.randint(0, len(nouns)-1)].strip().capitalize()
                else:
                    output += nouns[random.randint(0, len(nouns)-1)].strip()
                output += " "
                output += adjectives[random.randint(0, len(adjectives)-1)].strip()
                output += " "
                output += verbs[random.randint(0, len(verbs)-1)].strip()
                if k != length-1:
                    output += " "
            output += ". "
        
        # Add new lines between paragraphs
        output += "\n\n\t"

    return output

if __name__=="__main__":
    print("Enter number of paragraphs:")
    paragraphs = int(sys.stdin.readline())
    print("Enter number of sentences:")
    sentences = int(sys.stdin.readline())
    print(essaymonkey(paragraphs, sentences))