__author__ = 'Chenyuan'

from random import randint

#class EssayMonkey contains three methods: readFile, generateSentence, and essayMonkey.
#readFile and generateSentence are internal methods called by essayMonkey.
#This program is designed to use the default thesauruses: EssayMonkeyVerbs.txt, EssayMonkeyNouns.txt, and EssayMonkeyAdjectives.txt
#In order to make the auto-generated sentences reasonable, a better approach is to use training sentences and machine learning algorithms to capture the relationship among words.
class EssayMonkey(object):

    #readFile method is used to read a comma delimited file and return a list of words.
    #Run time complexity: big theta(1)
    #Pre-condition: fName is a working file directory and the file is comma delimited.
    #Post-condition: return a list of words
    def readFile(this_object, fName):
        words = list()
        with open(fName) as f:
            #read the file line by line
            content = f.readlines()
            for line in content:
                #delete the newline at the end of the paragraph
                line = line.replace("\n", "")
                words = words + line.split(",")
        return words

    #generateSentence method is used generate and return one type of sentence.
    #Run time complexity: big theta(1).
    #Pre-condition: num is a integer and among 0 to 5.
    #Post-condition: return one type of sentence.
    def generateSentence(this_object, num):
        sentence = None

        #create a verb pool, a noun pool, and a adjective pool
        verbs = this_object.readFile("EssayMonkeyVerbs.txt")
        nouns =this_object. readFile("EssayMonkeyNouns.txt")
        adjs =this_object. readFile("EssayMonkeyAdjectives.txt")

        #Choose a random noun
        noun = nouns[randint(0,len(nouns) - 1)]
        #Choose two more random nouns
        noun2 = nouns[randint(0,len(nouns) - 1)]
        noun3 = nouns[randint(0,len(nouns) - 1)]
        #Choose a random adjective
        adj = adjs[randint(0, len(adjs) - 2)]
        #Choose a random verb
        #Since there is only one "shall" in the verb pool, the program won't be able to choose the tense of the verb based on if the index is odd or even.
        verb = verbs[randint(0,len(verbs) - 1)]
        if "/" in verb:
            verb = verb.split("/")[randint(0,1)]


        #Capitalize the first character of the noun
        nounUpper = noun[0].upper() + noun[1:]
        #Capitalize the first character of the adjective
        adjUpper = adj[0].upper() + adj[1:]

        #Sentence patterns
        #pattern "noun + verb"
        if num == 0:
            sentence = nounUpper + " " + verb + ". "

        #pattern "adjective + noun + verb"
        elif num == 1:
            sentence = adjUpper + " " + noun + " " + verb + ". "

        #pattern "noun + verb + noun"
        elif num == 2:
            sentence = nounUpper + " " + verb + " " + noun2 + ". "

        #pattern "adj + noun + verb + noun"
        elif num == 3:
            sentence = adjUpper + " " + noun + " " + verb + " " + noun2 + ". "

        #pattern "Must + noun + and + noun + verb?"
        elif num == 4:
            sentence = "Must " + noun + " and " + noun2 + " " + verb + "? "

       #pattern "noun + verb + noun + with + noun"
        elif num == 5:
            sentence = nounUpper + " " + verb + " " + noun2 + " with " + noun3 + ". "

        return sentence

    #essayMonkey accepts user input of the number of paragraphs to generate and the number of sentences per paragraph.
    #It calls generateSentence and print out the sentences generateSentence return.
    #Run time complexity: big theta(N*M)
    #Pre-condition: enough memory.
    #Post-condition: an essay with N paragraphs and M sentences per paragraph is generated.
    def essayMonkey(this_object):
        #Accept user's integer input
        while True:
            try:
                numPara  = int(input("Please enter the number of paragraphs to generate: "))
                numSent = int(input("Please enter the number of sentences per paragraph to generate.: "))
                print()
                break
            except ValueError:
                print("Please enter integers.")

        #Generate the essay
        for i in range(1,numPara + 1):
            for j in range(1,numSent + 1):
                print(this_object.generateSentence(randint(0,5)), end = "")
            print()
            print()


#start the program by creating an instance of the class and use the instance to call essayMonkey
run = EssayMonkey()
run.essayMonkey()
