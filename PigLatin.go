package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strings"
	"unicode"
)

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

//OLD VERSION---
//find which indexes of the word are punctuation
//Returns a map of key/value pairs with byte[index int]
//index is based from the end of the word by subtracting the original index from len(word) -1
//

//MAIN

// ParseWords() << Returns a list of tokens

func main() {
	words, hyphens := ParseWords()

	for i, word := range words {
		if IsValid(&word) {
			word = *Translate(&word)
		}
		if hyphens[i] {
			fmt.Printf("\b-%s", word)
		} else {
			fmt.Printf("%s ", word)
		}
	}
}

func IsValid(word *string) bool {

	if (len(*word) == 1) || (*word == "") {
		return false
	}

	//Strip all the puctuation out of the word temporarily
	//and see if the word ends in "way"
	var buffer bytes.Buffer
	for _, c := range []byte(*word) {
		if IsAlpha(c) {
			buffer.WriteByte(c)
		}
	}
	tmp := buffer.String()
	if len(tmp) >= 3 {
		if string(tmp[len(tmp)-3:len(tmp)]) == "way" {
			return false
		}
	}
	return true
}

func ParseWords() ([]string, []bool) {

	var lines []string
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	var words []string
	var hyphens []bool
	for _, l := range lines {
		words = strings.FieldsFunc(l, func(c rune) bool {
			switch c {
			case ' ', '\n':
				return true
			}
			return false
		})
	}
	for i, w := range words {

		if strings.Contains(w, "-") {
			tmp := strings.Split(w, "-")
			words = append(append(words[0:i-1], tmp...), words[i+1:]...)
			hyphens = append(hyphens, true)
		} else {
			hyphens = append(hyphens, false)
		}
	}

	fmt.Println(len(words))
	fmt.Println(len(hyphens))
	return words, hyphens
}

func Translate(word *string) *string {

	var i int
	var startsWithPunc bool
	originalWord := *word
	newWord := []byte(originalWord)
	caps := []int{}
	for j, c := range newWord {
		if unicode.IsUpper(rune(c)) {
			caps = append(caps, j)
			i++
		}
	}
	newWord = bytes.ToLower(newWord)
	//Find the index of the first alphabetical byte

	//Worst case scenario is if a word has many punctuation before
	//the first letter.
	i = 0
	for !IsAlpha(originalWord[i]) && i < len(originalWord) {
		i++
		startsWithPunc = true
	}
	firstLetter := originalWord[i]

	//If the first letter is a consonant, slice and dice and add
	// "ay" to the end.
	if IsConsonant(newWord[i]) {
		newWord = append(append(newWord[i+1:], newWord[i]), []byte("ay")...)
	} else {
		newWord = append(newWord, []byte("way")...)
	}

	for i, c := range newWord {
		//For each punctuation in the word, add to it's index
		//to insert based on the following criteria:
		//
		//If the punctuation is the first byte in the word && the
		//first letter is a consonant, add two to the index
		//
		//else if the punc is last in the original word, move
		//it to the end of the new word
		//
		//else add three to the index of the puctuation

		//Using bytes.Buffer to save memory and runtime.
		if !IsAlpha(c) {
			var buffer bytes.Buffer
			if startsWithPunc && IsConsonant(firstLetter) && i == 0 {
				buffer.WriteString(string(newWord[1:2]))
				buffer.WriteString(string(newWord[0]))
				buffer.WriteString(string(newWord[3:]))
				newWord = []byte(buffer.String())
			} else if c == byte(originalWord[(len(originalWord)-1)]) {
				buffer.WriteString(string(newWord[0:i]))
				buffer.WriteString(string(newWord[i+1:]))
				buffer.WriteString(string(newWord[i]))
				newWord = []byte(buffer.String())
			} else {
				buffer.WriteString(string(newWord[0:i]))
				buffer.WriteString(string(newWord[i+1 : i+4]))
				buffer.WriteString(string(newWord[i]))
				buffer.WriteString(string(newWord[i+4:]))
				newWord = []byte(buffer.String())
			}
		}
	}

	//Alter the word to have the correct capitalization based on the
	//rules in PigLatin.md
	if len(caps) != 0 {
		for _, j := range caps {
			if IsAlpha(newWord[j]) {
				newWord[j] = byte(unicode.ToUpper(rune(newWord[j])))
			}
		}
	}
	retVal := string(newWord)
	return &retVal
}

func IsAlpha(char byte) bool {
	char = byte(unicode.ToLower(rune(char)))
	if char < 'a' || char > 'z' {
		return false
	}
	return true
}

func IsConsonant(char byte) bool {

	switch unicode.ToLower(rune(char)) {
	case 'a', 'e', 'i', 'o', 'u':
		return false
	}
	return true

}
