package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"math/rand"
	"strings"
)

const (
	STRING_MIN_LENGTH int = 10

	ADJECTIVE_FILEPATH string = "./adjectives.txt"
	VERB_FILEPATH      string = "./verbs.txt"
	NOUN_FILEPATH      string = "./nouns.txt"

	PARAGRAPH_SEP string = "\r\n\r\n    "
)

var ADJ_LIST, VERB_LIST, NOUN_LIST []string

func main() {
	processWordFiles()

	var numParagraphs, numSentences int

	fmt.Printf("Enter the number of paras to generate and sentences per para: ")
	_, err := fmt.Scanf("%d %d", &numParagraphs, &numSentences)
	check(err)

	output := generateParagraphs(numParagraphs, numSentences)

	fmt.Println("Output:\n"+ output)
}

// generateParagraphs creates paragraphs using the adjectives, verbs and nouns
// list. It selects the words randomly from any of the above lists add creates
// a formatted sentence. The sentence is added to the para if its of unique
// length and is also satisfying minimum length requiremnts
func generateParagraphs(numParagraphs, numSentences int) string {
	//var output bytes.Buffer
	data := make([][]string, 3)

	//adjectives
	data[0] = ADJ_LIST
	//verbs
	data[1] = VERB_LIST
	//nouns
	data[2] = NOUN_LIST

	isLenAvailable := make(map[int]bool)
	paragraphsArr := []string{}
	sentencesArr := []string{}
	totalNumSentences := numParagraphs * numSentences

	sentences := 0
	for sentences < totalNumSentences {
		var sentence bytes.Buffer
		wordsArr := []string{}
		for {
			setNumber := random(0, len(data))
			wordNumber := random(0, len(data[setNumber])-2)

			sentence.WriteString(data[setNumber][wordNumber])
			wordsArr = append(wordsArr, data[setNumber][wordNumber])

			length := len(sentence.String())
			if length >= STRING_MIN_LENGTH && isLenAvailable[length] == false {
				isLenAvailable[length] = true

				sentencesArr = append(sentencesArr, formatWords(&wordsArr))
				sentences++

				if (sentences != totalNumSentences && sentences%numSentences == 0) || (sentences == totalNumSentences) {
					paragraphsArr = append(paragraphsArr, formatSentences(&sentencesArr))

					// Emptying out the slice
					sentencesArr = sentencesArr[:0]
				}
				break
			}
			sentence.WriteString(" ")
		}
	}

	output := formatParagraphs(&paragraphsArr)
	return output
}

// formatWords takes reference to array of strings containing words and creates a
// formatted sentence using the words. It changes to first char to title case.
func formatWords(wordsArr *[]string) string {
	sentence := strings.Join(*wordsArr, " ")

	// Converting to title case
	return strings.ToTitle(string(sentence[0])) + sentence[1:]
}

// formatSentences takes reference to array of string containing sentences.
// It formats the sentences to be present in a single paragraph by joinging the
// sentences and adding "." where required.
func formatSentences(sentencesArr *[]string) string {
	return strings.Join(*sentencesArr, ". ") + "." // The last one is needed for the final sentence
}

// formatParagraphs takes reference to array of string containing paras. It formats
// the paras by joining them and inserting appropriate paragraph separator.
func formatParagraphs(paragraphsArr *[]string) string {
	return "    " + strings.Join(*paragraphsArr, PARAGRAPH_SEP) // Spaces in front are needed for first para
}

// processWordFiles reads the files containing adjectives, nouns and verbs to
// build separate list containing these words
func processWordFiles() {
	ADJ_LIST = readAndProcessFiles(ADJECTIVE_FILEPATH)
	VERB_LIST = readAndProcessFiles(VERB_FILEPATH)
	NOUN_LIST = readAndProcessFiles(NOUN_FILEPATH)
}

// readAndProcessFiles processes a file and returns the words in a file
func readAndProcessFiles(path string) []string {
	data, err := ioutil.ReadFile(path)
	check(err)

	dataList := strings.Split(string(data), ",")

	// Sanitizing the input.
	respData := []string{}
	for _, s := range dataList {
		if s != "" {
			respData = append(respData, strings.Trim(s, " \n\r\t,"))
		}
	}

	return respData
}

// check if the error is present or not. If yes, panic!
func check(e error) {
	if e != nil {
		panic(e)
	}
}

// random generates a random number between range from min to max (inclusive)
func random(min, max int) int {
	return rand.Intn(max-min) + min
}
