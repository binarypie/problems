import sys

def findpospunc(word):
    """
    Finds position of punctuation from end of word
    """
    for i in range(0, len(word)):
        if word[i] == "?" or word[i] == "!" or word[i] == "," or word[i] == "." or word[i] == "'":
            return len(word)-i-1

def piglatin(sentence):
    word_list = sentence.split()
    output = ""
    # Iterate over every word in the sentence
    for word in word_list:
        string_list = word.split("-")
        output_str = ""
        # Iterate over every word in a hyphenated word
        for string in string_list:
            out = ""
            lower_str = string.lower()
            vowels = ["a", "e", "i", "o", "u"]

            # Find punctuation
            puncpos = findpospunc(lower_str)
            if puncpos is not None:
                punc = lower_str[len(lower_str)-puncpos-1]

            # Handle the translation cases
            if len(lower_str) is 1 or lower_str[len(lower_str)-3:] == "way":
                out = lower_str
            elif vowels.count(lower_str[0]):
                if puncpos is not None:
                    out = lower_str[:len(lower_str)-puncpos-1]+lower_str[len(lower_str)-puncpos:]+"way"
                    out = out[:len(out)-puncpos]+punc+out[len(out)-puncpos:]
                else:
                    out = lower_str + "way"
            else:
                if puncpos is not None:
                    out = lower_str[1:len(lower_str)-puncpos-1]+lower_str[len(lower_str)-puncpos:]+lower_str[0]+"ay"
                    out = out[:len(out)-puncpos]+punc+out[len(out)-puncpos:]
                else:
                    out = lower_str[1:]+lower_str[0]+"ay"

            # Recapitalize
            tmp = ""
            for i in range(0, len(string)):
                if string[i].isupper():
                    tmp += out[i].upper()
                else:
                    tmp += out[i]
            if len(tmp) is not len(out):
                tmp += out[len(tmp):]

            out = tmp

            # Add hyphens back in
            if len(output_str) > 0:
                output_str += "-"
            output_str += out

        # Add transformed words back into sentence
        if len(output) is 0:
            output += output_str
        else:
            output = output + " " + output_str

    return output

if __name__=="__main__":
    print("Enter sentence or paragraph:")
    print(piglatin(sys.stdin.readline()))