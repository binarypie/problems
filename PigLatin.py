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

if __name__ == "__main__":
    
    input_string = raw_input("Please enter a string to convert: ")
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""

    words = input_string.split(' ')
    
    for word in words:
        if "-" in word:
            more_words = word.split("-")
            for new_word in more_words:
                result += loop(new_word, True)
        else:
            result += loop(word, False)
        
    print(result)
    