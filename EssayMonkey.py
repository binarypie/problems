#Function: Program creates an essay based off of files of nouns, verbs, and adjectives
#FunctionCont: randomizes the number of words per sentence, sentences per word, and number of paragraphs
#Coder: David Rodriguez
#Version: 1.2
#Date of last update: 2/23/2017
#Requirements: Please have EssayMonkeyNouns.txt, EssayMonkeyAdjectives.txt, and EssayMonkeyVerbs.txt
#RequirementsCont: in the same folder as the EssayMonkey.py file

import random

f_noun = open( 'EssayMonkeyNouns.txt' ) # opens EssayMonkeyNouns.txt file
f_verb = open( 'EssayMonkeyAdjectives.txt' ) # opens EssayMonkeyAdjectives.txt file
f_adj = open( 'EssayMonkeyVerbs.txt' ) # opens EssayMonkeyVerbs.txt file

d_noun = f_noun.read() # assigns the text file content to d_noun
d_verb = f_verb.read() # assigns the text file content to d_verb
d_adj = f_adj.read() # assigns the text file content to d_adj

w_noun = d_noun.split( ',' ) # splits the words into list w_noun
w_verb = d_verb.split( ',' ) # splits the words into list w_vern
w_adj = d_adj.split( ',' ) # splits the words into list w_noun

len_noun = len( w_noun ) # finds the length of w_noun
len_verb = len( w_verb ) # finds the length of w_verb
len_adj = len( w_adj ) # finds the length of w_adj

def Essay ( n_par, n_lines ):

    c_par =0
    ess_out = ''

    while ( c_par < n_par ):
        c_lines = 0
        para = ''

        while ( c_lines < n_lines):
            c_words = 0
            sent = ''
            n_word = random.randint( 9, 17 ) # set to randomly make each sentence to have 9 - 17 words
                                              # please change the numbers above if you want to set a different sentence length
            while ( c_words < n_word ):
                rand = random.randint( 1, 3 )

                if ( rand == 1 ) :
                    sent +=  w_noun[ random.randint ( 1, len_noun - 1 ) ]

                elif( rand == 2 ) :
                    sent +=  w_verb[ random.randint ( 1, len_verb - 1 ) ]

                else:
                    sent +=  w_adj[random.randint ( 1, len_adj - 1 ) ]

                if( c_words != n_word - 1 ):
                    sent += ' '

                c_words += 1

            sent += '.\n'
            para += sent
            c_lines += 1

        para += '\n'
        para += '\n'
        ess_out += para
        c_par += 1

    return ess_out


n_par = int( input( '\nPlease enter the number of paragraphs to generate: ' ) )
n_lines = int( input ( 'Please enter the number of sentences to generate: ' ) )

ess_out = Essay ( n_par, n_lines)

print ( 'Below is an Essay with ', n_par, ' paragraphs and ', n_lines, ' sentences per paragraph:\n' )
print ( ess_out )