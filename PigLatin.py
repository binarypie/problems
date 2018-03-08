# coding: utf-8
# Words that start with a consonant have their first letter moved to the end of the word and the letters “ay” added to the end.
# Words that start with a vowel have the letters “way” added to the end.
# Words that end in “way” are not modified.
# Punctuation must remain in the same relative place from the end of the word.
# Hyphens are treated as two words
# Capitalization must remain in the same place.
# Single letters are not modified.

# result = "ElLOhay Orldway! I antca'y aitway otay exploreway ouryay ASTVay orestfay. Hetay-Endway!"

def loop(word, hyphen):
    
    result = ""
    
    lower_word = word.lower()
    
    if len(lower_word) == 1 or lower_word[-3:] == "way":
        result += word
    
    elif lower_word[0] in vowels:
        result += word + "way"
    
    else:
        new_word = word[1:] + word[0]
        for i in range(len(word)):
            if word[i].isupper():
                result += new_word[i].upper()
            else:
                result += new_word[i].lower()
        result += "ay"
    
    if hyphen:
        result += "-"
    else:
        result += " "
        
    return result

string = "Hello world!"
bigstring = "HeLLo World! I can't wait to explore your VAST forests. The-End!"

vowels = ['a', 'e', 'i', 'o', 'u']
result = ""

words = bigstring.split(' ')

for word in words:
    if "-" in word:
        more_words = word.split("-")
        for new_word in more_words:
            result += loop(new_word, True)
    else:
        result += loop(word, False)
    
print(result)
    