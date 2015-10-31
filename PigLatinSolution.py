import re
import string

vowels = ['a', 'e', 'i', 'o', 'u']


# parses one word into pig latin
def parse(in_word):
    # word without punctuation
    no_punct = "".join(p for p in in_word if p not in string.punctuation)

    if len(in_word) == 1:
        out_word = in_word
    elif no_punct.endswith("way"):
        out_word = in_word
    elif is_vowel(in_word[0]) is True:
        # word starting with vowel have "way" added to the end
        out_word = no_punct + "way"

        # add in punctuation
        out_word = keep_punct(in_word, out_word, 3)
    else:
        # word starts with consonant
        # record upper or lowercase for indices
        case = []
        for ch in in_word:
            if str.isupper(ch):
                case.append(1)
            else:
                case.append(0)

        # move first letter to the end
        np_list = list(no_punct)
        del np_list[0]
        np_list.append(no_punct[0])

        # add ay to the end
        out = ''.join(np_list)
        out += "ay"

        # add in punctuation
        out = keep_punct(in_word, out, 2)

        # change the cases to match original
        final_out = list(out)
        for ind, x in enumerate(case):
            change = out[ind]
            if x == 1:
                final_out[ind] = str.upper(change)
            else:
                final_out[ind] = str.lower(change)
        out_word = ''.join(final_out)

    return out_word


# keep punctuation same relative place from the end of word
def keep_punct(in_word, out, num):
    indexes = re.finditer("\W", in_word)
    for i in indexes:
        ind = i.start()
        out = out[:ind+num] + in_word[ind] + out[ind+num:]
    return out


# check if character is vowel
def is_vowel(ch):
    if str.lower(ch) in vowels:
        return True
    return False


if __name__=="__main__":

    running = True
    while running:
        user_input = raw_input("Enter your string to translate or QUIT to exit program: ")
        if user_input == "QUIT":
            running = False
        else:
            words = user_input.split()

            # record where hyphens are
            hyphen = list([])
            count = 0
            for ind, word in enumerate(words):
                for w in word:
                    if w is '-':
                        hyphen.append(ind+count)
                        count += 1

            # take out the hyphens
            user_input = user_input.replace('-',' ')
            words = user_input.split()

            # parse words then concatenate
            output = ""
            for ind, word in enumerate(words):
                if ind in hyphen:
                    output += parse(word) + "-"
                else:
                    output += parse(word) + " "
            print output
