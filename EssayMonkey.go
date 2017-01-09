package essaymonkey

import (
	"bytes"
	"io/ioutil"
	"log"
	"math/rand"
	"strings"
	"time"
	"unicode"
)

//I have to say, I appreciated this problem. It was a bit more in depth than
//what was requested, but I had fun with it!

//Sentence structures:
//A = Adjective
//N = Nouns
//V = Verbs

//A N V "and" A N V
//A N PastTenseV
//A N PastTenseV "and" either of the above

//Adjectives may chain together, or be left out altogether.
//"but" may be used to join multiple sentences

const adjectiveFileName = "EssayMonkeyAdjectives.txt"
const verbFileName = "EssayMonkeyVerbs.txt"

//Swap these for a little Mass Effect fun.

const nounFileName = "EssayMonkeyNouns.txt"

//const nounFileName = "EssayMonkeyCharacters.txt"

var adjectives, nouns []string

func Generate(numParagraphs int, numSentences int) *string {

	//Reads the EssayMonkeyVerbs.txt file and splits the file into two seperate
	//arrays for past/present tense
	presentTense, pastTense := readWords(verbFileName, func(words []string) ([]string, []string) {
		var presentTense []string
		var pastTense []string
		for i := 0; i < len(words)-1; i += 2 {
			presentTense = append(presentTense, words[i])
			pastTense = append(pastTense, words[i+1])
		}
		return presentTense, pastTense
	})

	//Reads the EssayMonkeysNouns.txt and splits it into two arrays based on word length.
	nouns, _ = readWords(nounFileName, func(words []string) ([]string, []string) {
		return words, nil
	})

	//Reads the EssayMonkeysAdjectives.txt and splits it into two arrays based on word length.
	adjectives, _ = readWords(adjectiveFileName, func(words []string) ([]string, []string) {
		return words, nil
	})

	var buffer bytes.Buffer
	for j := 0; j < numParagraphs; j++ {
		for i := 0; i < numSentences; i++ {

			//Generate all of our sentance structure bearing pseudo-random variables
			rand.Seed(time.Now().UnixNano())
			and := rand.Intn(2) == 1
			but := rand.Intn(2) == 1
			verbPastTense := rand.Intn(2) == 1

			if i == 0 {
				buffer.WriteString("\t")
			}

			//Have to capitalize the first letter!
			adjNouns := []byte(addAdjNouns())
			adjNouns[0] = byte(unicode.ToUpper(rune(adjNouns[0])))
			buffer.WriteString(string(adjNouns))

			//Structure logic
			if and {
				buffer.WriteString("and ")
				buffer.WriteString(addAdjNouns())

				if verbPastTense {
					buffer.WriteString(pastTense[rand.Intn(len(pastTense)-1)])
				} else {
					buffer.WriteString(presentTense[rand.Intn(len(presentTense)-1)])
				}
				and = rand.Intn(1) == 1
			} else {
				buffer.WriteString(pastTense[rand.Intn(len(pastTense)-1)])
			}
			if but {
				buffer.WriteString(" ")
				buffer.WriteString("but ")
				buffer.WriteString(addAdjNouns())
				if and {
					buffer.WriteString("and ")
					buffer.WriteString(addAdjNouns())
					if verbPastTense {
						buffer.WriteString(pastTense[rand.Intn(len(pastTense)-1)])
					} else {
						buffer.WriteString(presentTense[rand.Intn(len(presentTense)-1)])
					}
				} else {
					buffer.WriteString(pastTense[rand.Intn(len(pastTense)-1)])
				}
				buffer.WriteString(". ")
			} else {
				buffer.WriteString(". ")
			}
		}
		buffer.WriteString("\n\n")
	}
	retVal := buffer.String()
	return &retVal
}

func addAdjNouns() string {

	var buff bytes.Buffer
	for j := 0; j < rand.Intn(3); j++ {
		buff.WriteString(adjectives[rand.Intn(len(adjectives)-1)])
		buff.WriteString(" ")
	}
	buff.WriteString(nouns[rand.Intn(len(nouns)-1)])
	buff.WriteString(" ")
	return buff.String()
}
func readWords(fileName string, sortFunc func(words []string) ([]string, []string)) ([]string, []string) {
	file, err := ioutil.ReadFile(fileName)
	checkErr(err)
	all := strings.Split(string(file), ",")
	return sortFunc(all)
}
func checkErr(err error) {
	if err != nil {
		log.Fatalln(err.Error())
	}
}
