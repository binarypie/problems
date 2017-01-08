package main

import "fmt"

//parse input into tokens including the punctuation and casing
//delimiters are: "\n" ,  " " , and "-"
//https://golang.org/pkg/strings/#Split

//check if token is a valid word which needs modified
//not valid if word ends in "way"
//not valid if word is only one letter
//not valid if there string is empty

//See if word starts with consonant
//If not return false

//See which indexes of the word are capitalized

//find which indexes of the word are punctuation

//MAIN

// ParseWords() << Returns a list of tokens

func main() {
	fmt.Println("vim-go")

	words := ParseWords()

	for word := range words {
		if word.IsValid() {
			capitalizedLetters := IndexOfCapitals()
			punc := IndexOfPunctuation()

			if IsConsonant(word[0]) {
				word = word[1:] + word[0] + "ay"

			} else {
				word = word + "way"
			}

			for i, c := range word {
				for _, j := range capitalizedLetter {
					if j == i {
						ToUpper(string(c))
					} else {
						ToLower(string(c))
					}
				}
				for _, j := range punctuation {
					j = len(word) - j
					if j == i {

					} else {

					}
				}
			}
		}
	}
}
