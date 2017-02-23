#Function: Program translates a word, sentence or paragraph of english text
#FunctionCont: into Pig Latin
#Coder: David Rodriguez
#Version: 1.3
#Date of last update: 2/22/2017
#ExampleIn: HeLLo World! I can't wait to explore your VAST forests. The-End!
#ExampleOut: ElLOhay Orldway! I antca'y aitway otay exploreway ouryay ASTVay orestfay. Hetay-Endway!
import string, re

vowel = ['a', 'e', 'x', 'o', 'u'] # list of vowels to use for search

def vowel_check(letter): # identifies if letter is a vowel
    if str.lower(letter) in vowel: # checks if letters are lower case or not
        return True
    return False

def pun_in(w_in, s_out, loc): # keep punctuation same relative place from the end of word
    indices = re.finditer("\W", w_in)
    for x in indices:
        index = x.start() # finds and stores the location of punctuation
        s_out = s_out[:index+loc] + w_in[index] + s_out[index+loc:]
    return s_out

def translate(w_in): # translates word
    w_no_pun = ''.join(a for a in w_in if a not in string.punctuation) # string without punctuation
    if len(w_in) == 1: # if length of word is 1
        w_out = w_in # then return the same word
    elif w_no_pun.endswith('way'): # if word ends with way
        w_out = w_in # then return the same word
    elif vowel_check(w_in[0]) is True:
        w_out = w_no_pun + 'way' # if the first letter is a vowel then add "way" to the end
        w_out = pun_in(w_in, w_out, 3)
    else:# checks if first letter is a consonant
        check_case = []
        for letter in w_in:
            if str.isupper(letter):
                check_case.append(1) # records uppercase indices
            else:
                check_case.append(0) # records lowercase indices
        fl_li = list(w_no_pun) # stores first consonant
        del fl_li[0]# deletes first consonant from the front
        fl_li.append(w_no_pun[0]) # adds the first consonant to end of word
        s_out = ''.join(fl_li)
        s_out += "ay" # adds ay after the first consonant at the end
        s_out = pun_in(w_in, s_out, 2) # re-adds punctuation
        f_out = list(s_out)
        for index, b in enumerate(check_case): # changes the case-ing to match the original location
            alter = s_out[index]
            if b == 1:
                f_out[index] = str.upper(alter)
            else:
                f_out[index] = str.lower(alter)
        w_out = ''.join(f_out)
    return w_out

if __name__=="__main__":
    running = True
    while running: # loop to allow the user to continue to translate multiple strings
        u_in = input('\nPlease enter a word, sentence, or paragraph to be translated or EXIT to end: ')
        if u_in == 'EXIT': # allows the user to break the loop
            print('\nNow Ending Program')
            running = False
        else:
            strings = u_in.split() # splits the string into words
            hyphens = list([]) # creates a list to store hyphen locations
            counter = 0
            for index, w_var in enumerate(strings):
                for y in w_var:
                    if y is '-':
                        hyphens.append(index+counter)# records hyphen location
                        counter += 1
            u_in = u_in.replace('-',' ') # removes the hyphens
            strings = u_in.split()  # splits the string into separate words
            f_out = ""
            for index, w_var in enumerate(strings): # translate the un-hyphenated words then returns the hyphen to the same location
                if index in hyphens:
                    f_out += translate(w_var) + "-"
                else:
                    f_out += translate(w_var) + " "
            print ('\nBelow is the Pig Latin translation of the user input: ')
            print (f_out) # prints out the translation
