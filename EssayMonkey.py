import sys
import random

def readFile(filename):
    fd = open(filename, "r")
    words = fd.read().split(",")
    fd.close()
    return words, len(words)

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Correct format is: python EssayMonkey.py <no_of_paragraphs> <no_of_sentences>")
        exit(1)
    
    paragraphs = int(sys.argv[1])
    sentences = int(sys.argv[2])
    
    verbs, verb_len = readFile("EssayMonkeyVerbs.txt")
    adjectives, adjective_len = readFile("EssayMonkeyAdjectives.txt")
    nouns, noun_len = readFile("EssayMonkeyNouns.txt")
    
    for i in range(paragraphs):
        paragraph = ""
        
        for j in range(sentences):
            num_words = random.randint(3, 10)       # 4, 5, 6, 7, 8, 9, 10
            sentence = ""
            
            while (num_words > 0):
                sentence += adjectives[random.randint(0, adjective_len - 1)]
                num_words -= 1
                if num_words > 0:
                    sentence += " "
                else:
                    sentence += ". "
                    break
                
                sentence += nouns[random.randint(0, noun_len - 1)]
                num_words -= 1
                if num_words > 0:
                    sentence += " "
                else:
                    sentence += ". "
                    break
                
                sentence += verbs[random.randint(0, verb_len - 1)]
                num_words -= 1
                if num_words > 0:
                    sentence += " "
                else:
                    sentence += ". "
                    break
            
            paragraph += sentence
        paragraph += "\n"
        print(paragraph)