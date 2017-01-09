package piglatin

import (
	"bufio"
	"bytes"
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

//determines whether or not the provided word needs translating
func IsValid(word *string) bool {

	if len(*word) <= 1 {
		return false
	}

	//Strip all the puctuation out of the word temporarily
	//and see if the word ends in "way"
	var buffer bytes.Buffer
	for _, c := range []byte(*word) {
		if IsAlpha(c) {
			buffer.WriteByte(byte(unicode.ToLower(rune(c))))
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

//Parses input from stdin until it recieves EOF
func ParseWords(input *string) []string {

	var words []string
	scanner := bufio.NewScanner(strings.NewReader(*input))
	scanner.Split(bufio.ScanBytes)
	var byteSlice []byte
	for i := 0; scanner.Scan(); i++ {
		byteSlice = append(byteSlice, scanner.Bytes()...)
	}

	var word []byte
	for _, b := range byteSlice {
		switch b {
		case ' ', '\n', '-':
			words = append(words, string(word))
			words = append(words, string(b))
			word = word[:0]
		default:
			word = append(word, b)
		}
	}
	//Just in case we miss the last word
	if len(word) > 1 {
		words = append(words, string(word))
	}
	return words

}

//converts a valid word into it's pig latin variant
func Translate(input *string) string {

	words := ParseWords(input)
	var buffer bytes.Buffer
	for _, word := range words {
		var wordBytes []byte
		if IsValid(&word) {
			var i int
			var startsWithPunc bool
			wordBytes = []byte(word)
			originalWord := word
			caps := []int{}
			for j, c := range word {
				if unicode.IsUpper(rune(c)) {
					caps = append(caps, j)
					i++
				}
			}
			wordBytes = bytes.ToLower(wordBytes)
			//Find the index of the first alphabetical byte

			//Worst case scenario is if a word has many punctuation before
			//the first letter.
			i = 0
			for !IsAlpha(wordBytes[i]) && i < len(wordBytes) {
				i++
				startsWithPunc = true
			}
			firstLetter := wordBytes[i]

			//If the first letter is a consonant, slice and dice and add
			// "ay" to the end.
			if IsConsonant(wordBytes[i]) {
				wordBytes = append(append(wordBytes[i+1:], wordBytes[i]), []byte("ay")...)
			} else {
				wordBytes = append(wordBytes, []byte("way")...)
			}

			for i, c := range wordBytes {
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
					var buff bytes.Buffer
					if startsWithPunc && IsConsonant(firstLetter) && i == 0 {
						buff.WriteString(string(wordBytes[1:2]))
						buff.WriteString(string(wordBytes[0]))
						buff.WriteString(string(wordBytes[3:]))
						wordBytes = []byte(buff.String())
					} else if c == byte(originalWord[(len(originalWord)-1)]) {
						buff.WriteString(string(wordBytes[0:i]))
						buff.WriteString(string(wordBytes[i+1:]))
						buff.WriteString(string(wordBytes[i]))
						wordBytes = []byte(buff.String())
					} else {
						buff.WriteString(string(wordBytes[0:i]))
						buff.WriteString(string(wordBytes[i+1 : i+4]))
						buff.WriteString(string(wordBytes[i]))
						buff.WriteString(string(wordBytes[i+4:]))
						wordBytes = []byte(buff.String())
					}
				}
			}

			//Alter the word to have the correct capitalization based on the
			//rules in PigLatin.md
			if len(caps) != 0 {
				for _, j := range caps {
					if IsAlpha(wordBytes[j]) {
						wordBytes[j] = byte(unicode.ToUpper(rune(wordBytes[j])))
					}
				}
			}
		} else {
			wordBytes = []byte(word)
		}
		buffer.WriteString(string(wordBytes))
	}
	return buffer.String()
}

//Determines if a given byte is a valid alphabetical letter.
func IsAlpha(char byte) bool {
	char = byte(unicode.ToLower(rune(char)))
	if char < 'a' || char > 'z' {
		return false
	}
	return true
}

//Determines if the provided letter is a consonant or not.
func IsConsonant(char byte) bool {

	switch unicode.ToLower(rune(char)) {
	case 'a', 'e', 'i', 'o', 'u':
		return false
	}
	return true

}
