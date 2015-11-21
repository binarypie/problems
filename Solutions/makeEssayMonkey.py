import sys
import random



def essayMaker(num_paragraphs, num_sentences):
    
    """ 
    Generates a random Monkey Essay given the number of paragraphs and 
    sentences in each paragraph
    Arguments: number of paragraph, number of sentences
    Return: Essay (String)
    
    """
    noun_file = open('EssayMonkeyNouns.txt', 'r')
    verb_file = open('EssayMonkeyVerbs.txt', 'r')
    adjective_file = open('EssayMonkeyAdjectives.txt','r')
    
    nouns_list = noun_file.read().strip('\n').split(',')
    verb_list = verb_file.read().strip('\n').split(',')
    adjective_list = adjective_file.read().strip('\n').split(',')
    
    mymap ={0:nouns_list, 1:verb_list, 2:adjective_list}
    
    paras =""
    while num_paragraphs>0:
        paras += makeParagraph(num_sentences, mymap) + "\n \n" 
        num_paragraphs -= 1
    
    return paras

def makeParagraph(num_sentences, mymap):
    """
    Makes a paragraph taking the number of sentences to hold in that paragraph
    Arguments: number of sentences, {Map of List to use to construct words in sentences}
    
    """
    
    paragraph = ""
    l = min(len(mymap[0]), len(mymap[1]), len(mymap[2]))
    
    a_rand = random.sample(range(2, l), num_sentences)
    #a_rand = set()
    #while len(a_rand) < num_sentences:
    #    a_rand.add(random.randint(3, l%12))
    
    sentences = []
    for i in range (0,num_sentences):
        sentences.append(makeSentence(mymap, a_rand[i]))
    paragraph = "\n".join(sentences)
    
    return paragraph

def makeSentence(mymap, num_words_in_sentence):
    sentence = ""
    i=0
    j=0
    while i<num_words_in_sentence:
        
        sentence += mymap[j%3][random.randint(0,len(mymap[j%3])-1)]+" "
        j+=1
        i+=1
        
    s = sentence.capitalize().strip()+"."
    return s
    
if __name__ == "__main__":
    
    print '\n'
    print "**********   Monkey Essay Maker *************"
    print '\n'
    
    
    num_paragraphs = int(sys.argv[1])
    num_sentences = int(sys.argv[2])
    
    p = essayMaker(num_paragraphs, num_sentences)
    print p
    
    