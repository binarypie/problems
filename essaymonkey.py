import random

def EssayMonkey(num_paragraphs, num_sentences):
    
    noun_file = open('EssayMonkeyNouns.txt', 'r')
    nouns_list = noun_file.read().strip('\n').split(',')
    noun_file.close()

    verb_file = open('EssayMonkeyVerbs.txt', 'r')
    verb_list = verb_file.read().strip('\n').split(',')
    verb_file.close()
    
    adjective_file = open('EssayMonkeyAdjectives.txt','r')
    adjective_list = adjective_file.read().strip('\n').split(',')
    adjective_file.close()
    
    mymap = {0:nouns_list, 1:verb_list, 2:adjective_list}
    
    paras = ""
    while num_paragraphs > 0:
        paras += "  " + makeParagraph(num_sentences, mymap) + "\n \n" 
        num_paragraphs -= 1
    
    return paras

def makeParagraph(num_sentences, mymap):
    
    paragraph = ""
    l = min(len(mymap[0]), len(mymap[1]), len(mymap[2]))
    
    a_rand = random.sample(range(2, l), num_sentences)
    
    sentences = []
    for i in range(0,num_sentences):
        sentences.append(makeSentence(mymap, a_rand[i]))
    paragraph = " ".join(sentences)
    
    return paragraph

def makeSentence(mymap, num_words_in_sentence):
    sentence = ""
    i = 0
    j = 0
    while i < num_words_in_sentence:
        if(j % 3 == 0):
            sentence += mymap[0][random.randint(0,len(mymap[0]) - 1)] + " "
        if(j % 3 == 1):
            sentence += mymap[1][random.randint(0,len(mymap[1]) - 1)] + " "
        if(j % 3 == 2):
            sentence += mymap[2][random.randint(0,len(mymap[2]) - 1)] + " "
        
        j+=1
        i+=1
    s = sentence.capitalize().strip() + "."
    return s
    
print('\n')
print("This is an Essay from Monkey with a Banana ;-)")
print('\n')
    
    
num_paragraphs = int(input("Enter the desired num of paragraphs to generate in the essay:"))
num_sentences = int(input("Enter the desired num of sentences to be in the paragraph:"))
    
p = EssayMonkey(num_paragraphs, num_sentences)
print(p)
