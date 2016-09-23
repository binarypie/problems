package problem

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

const (
	period  = "."
	space   = " "
	newline = "\n"

	fileAdjectives = "./EssayMonkeyAdjectives.txt"
	fileNouns      = "./EssayMonkeyNouns.txt"
	fileVerbs      = "./EssayMonkeyVerbs.txt"
)

// Essay represents an essay. Its capacity indicates the number of paragraphs it must have.
type Essay struct {
	capacity   int
	paragraphs []paragraph
	wordBank
}

// NewEssay returns a new instance of Essay.
func NewEssay(capacity, paragraphCapacity int) *Essay {
	essay := &Essay{
		capacity: capacity,
	}

	for i := 0; i < essay.capacity; i++ {
		essay.paragraphs = append(essay.paragraphs, paragraph{capacity: paragraphCapacity})
	}
	return essay
}

// Build constructs an essay from the given list of words.
func (e *Essay) Build(words ...string) error {
	if len(words) == 0 {
		if err := e.Load(fileAdjectives, fileNouns, fileVerbs); err != nil {
			return err
		}
		words = e.Compose()
	}

	var errors []error
	wordCapacityPerParagraph := e.wordCount(words) / e.capacity
	for i, start, end := 0, 0, wordCapacityPerParagraph; i < e.capacity; i++ {
		if e.isLastParagraph(i) {
			end = len(words)
		}

		if err := e.paragraphs[i].build(words[start:end]...); err != nil {
			errors = append(errors, err)
		}
		start, end = wordCapacityPerParagraph*(i+1), wordCapacityPerParagraph*(i+2)
	}

	var errStr string
	for _, e := range errors {
		errStr = fmt.Sprintf("%s\n", e)
	}

	if errStr != "" {
		return fmt.Errorf("%s", errStr)
	}
	return nil
}

func (e *Essay) isLastParagraph(counter int) bool {
	return counter == e.capacity-1
}

func (e *Essay) wordCount(words []string) int {
	return len(words)
}

// String returns a string representation of essay.
func (e *Essay) String() string {
	var str string
	for _, p := range e.paragraphs {
		str += p.String() + newline
	}
	return str
}

// paragraph represents a paragraph in an essay. Its capacity indicates the number of sentences it must have.
type paragraph struct {
	capacity  int
	sentences []sentence
}

// Build constructs a paragraph from the given words.
// It returns an error when there aren't enough words for p to satisfy its capacity.
func (p *paragraph) build(words ...string) error {
	limit := p.sentenceCapacity(len(words))
	if limit == 0 {
		return fmt.Errorf("Not enough words to build a paragraph with %d sentences.", p.capacity)
	}

	var count int
	var s sentence
	for index, word := range words {
		if p.isLastSentence(count) {
			s.add(words[index:]...)
			p.add(s)
			break
		}

		if s.wordCount() < limit {
			s.add(word)
		}

		if s.wordCount() >= limit || index == len(words)-1 {
			p.add(s)
			s = ""
			count++
		}
	}
	return nil
}

func (p *paragraph) sentenceCapacity(numWords int) int {
	return int(math.Floor(float64(numWords) / float64(p.capacity)))
}

func (p *paragraph) add(s sentence) {
	p.sentences = append(p.sentences, s)
}

func (p *paragraph) isLastSentence(count int) bool {
	return count == p.capacity-1
}

// String returns a string representation of paragraph.
func (p *paragraph) String() string {
	var str string
	for _, s := range p.sentences {
		str += strings.TrimSpace(s.String()) + period + space
	}
	return strings.TrimSpace(str)
}

// sentence represents a sentence in a paragraph.
type sentence string

func (s *sentence) add(words ...string) *sentence {
	for _, word := range words {
		*s += sentence(word + space)
	}
	return s
}

// String returns a string representation of sentence.
func (s *sentence) String() string {
	return string(*s)
}

func (s *sentence) wordCount() int {
	return strings.Count(string(*s), space)
}

// wordBank contains all the words that an essay can draw from.
// It implements the Composer interface to  define the strategy to compose an essay.
type wordBank struct {
	dictionary map[string][]string
	Composer
}

// Load reads the content of the adjectivesFile, nounsFile and verbsFile and
// grouped them accordingly in an internal map.
func (w *wordBank) Load(adjectivesFile, nounsFile, verbsFile string) error {
	w.dictionary = make(map[string][]string)

	adjectives, err := ioutil.ReadFile(adjectivesFile)
	if err != nil {
		return err
	}

	adjectives = bytes.Replace(adjectives, []byte(","), []byte(" "), -1)
	w.dictionary["adjectives"] = strings.Split(string(adjectives), " ")

	nouns, err := ioutil.ReadFile(nounsFile)
	if err != nil {
		return err
	}

	nouns = bytes.Replace(nouns, []byte(","), []byte(" "), -1)
	w.dictionary["nouns"] = strings.Split(string(nouns), " ")

	verbs, err := ioutil.ReadFile(verbsFile)
	if err != nil {
		return err
	}

	sanitizedVerbs := w.sanitizeVerbs(string(verbs))
	w.dictionary["verbs"] = strings.Split(sanitizedVerbs, " ")

	return nil
}

// Compose uses a predefined strategy to compose a series of strings into an essay.
func (w *wordBank) Compose() []string {
	adjectives := w.dictionary["adjectives"]
	nouns := w.dictionary["nouns"]
	verbs := w.dictionary["verbs"]

	var composition []string
	for i := 0; i < len(adjectives); i++ {
		composition = append(composition, adjectives[i])

		if i < len(nouns) {
			composition = append(composition, nouns[i])
		}

		if i < len(verbs) {
			composition = append(composition, verbs[i])
		}
	}

	return composition
}

func (w *wordBank) sanitizeVerbs(verbs string) string {
	sanitized := strings.Replace(verbs, "used (to)", "used,used to", -1)
	sanitized = strings.Replace(sanitized, ",", " ", -1)
	sanitized = strings.Replace(sanitized, "/", " ", -1)
	sanitized = strings.Replace(sanitized, "\t", "", -1)
	return strings.TrimSpace(sanitized)
}

// A Composer provides the Compose interface to compose a series of strings into an essay.
// It doesn't take any argument as it assumes the receiver has a member variable that holds the
// strings.
type Composer interface {
	Compose() []string
}
