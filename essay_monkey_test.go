package problems

import (
	"fmt"
	"io/ioutil"
	"strings"
	"testing"
)

func TestBuildEssayWithFileInputs(t *testing.T) {
	numParagraphs, numSentencesPerParagraphs := 5, 10
	essay := NewEssay(numParagraphs, numSentencesPerParagraphs)
	if err := essay.Build(); err != nil {
		t.Fatal("Unexpected error", err)
	}

	if essay == nil {
		t.Error("Expected essay not to be empty")
	}
}

func TestBuildEssay(t *testing.T) {
	t.Run("Given enough words to build an essay that satisfies its capacity", func(t *testing.T) {
		var tests = []struct {
			limitParagraphs            int
			limitSentencePerParagraphs int
			words                      []string
			expected                   string
		}{
			{limitParagraphs: 1,
				limitSentencePerParagraphs: 1,
				words:    []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
				expected: "fat red thin cat sun thread meows glows jumps.\n"},
			{limitParagraphs: 2,
				limitSentencePerParagraphs: 1,
				words:    []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
				expected: "fat red thin cat.\nsun thread meows glows jumps.\n"},
			{limitParagraphs: 3,
				limitSentencePerParagraphs: 1,
				words:    []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
				expected: "fat red thin.\ncat sun thread.\nmeows glows jumps.\n"},
			{limitParagraphs: 4,
				limitSentencePerParagraphs: 1,
				words:    []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
				expected: "fat red.\nthin cat.\nsun thread.\nmeows glows jumps.\n"},
			{limitParagraphs: 5,
				limitSentencePerParagraphs: 1,
				words:    []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
				expected: "fat.\nred.\nthin.\ncat.\nsun thread meows glows jumps.\n"},
			{limitParagraphs: 1,
				limitSentencePerParagraphs: 2,
				words:    []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
				expected: "fat red thin cat. sun thread meows glows jumps.\n"},
			{limitParagraphs: 2,
				limitSentencePerParagraphs: 2,
				words:    []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
				expected: "fat red. thin cat.\nsun thread. meows glows jumps.\n"},
			{limitParagraphs: 3,
				limitSentencePerParagraphs: 2,
				words:    []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
				expected: "fat. red thin.\ncat. sun thread.\nmeows. glows jumps.\n"},
			{limitParagraphs: 4,
				limitSentencePerParagraphs: 2,
				words:    []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
				expected: "fat. red.\nthin. cat.\nsun. thread.\nmeows. glows jumps.\n"},
		}

		for id, test := range tests {
			essay := NewEssay(test.limitParagraphs, test.limitSentencePerParagraphs)
			if err := essay.Build(test.words...); err != nil {
				t.Fatal("Unexpected error: ", err)
			}

			actual := fmt.Sprintf("%s", essay)
			if actual != test.expected {
				t.Errorf("Mismatch essay. Bad test #%d\n\t- Expected %q\n\t- But got %q", id, test.expected, actual)
			}
		}
	})

	t.Run("Given not enough words to build an essay that satisfies its capacity", func(t *testing.T) {
		var tests = []struct {
			limitParagraphs            int
			limitSentencePerParagraphs int
			words                      []string
		}{
			{limitParagraphs: 5,
				limitSentencePerParagraphs: 2,
				words: []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"},
			},
		}

		for _, test := range tests {
			essay := NewEssay(test.limitParagraphs, test.limitSentencePerParagraphs)
			if err := essay.Build(test.words...); err == nil {
				t.Errorf("Expected error didn't occur. Should have failed to build an error since there aren't enough words to build a essay with %d paragraph and %d sentences per paragraph.", test.limitParagraphs, test.limitSentencePerParagraphs)
			}
		}
	})
}

func TestBuildParagraph(t *testing.T) {
	t.Run("Given enough words to build a paragraph that satisfies its capacity", func(t *testing.T) {
		var tests = []struct {
			words    []string
			expected string
			capacity int
		}{
			{words: []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"}, capacity: 1, expected: "fat red thin cat sun thread meows glows jumps."},
			{words: []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"}, capacity: 2, expected: "fat red thin cat. sun thread meows glows jumps."},
			{words: []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"}, capacity: 3, expected: "fat red thin. cat sun thread. meows glows jumps."},
			{words: []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"}, capacity: 4, expected: "fat red. thin cat. sun thread. meows glows jumps."},
			{words: []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"}, capacity: 5, expected: "fat. red. thin. cat. sun thread meows glows jumps."},
		}

		for _, test := range tests {
			p := &paragraph{capacity: test.capacity}
			if err := p.build(test.words...); err != nil {
				t.Fatal("Unexpected error: ", err)
			}

			actual := fmt.Sprintf("%s", p)
			if actual != test.expected {
				t.Errorf("Mismatch paragraph. Bad inputs %v, capacity=%d. Expected %q, but got %q", test.words, test.capacity, test.expected, actual)
			}
		}
	})

	t.Run("Given not enough words to build a paragraph that satisfies its capacity", func(t *testing.T) {
		var tests = []struct {
			words    []string
			expected string
			capacity int
		}{
			{words: []string{}, capacity: 1, expected: "fat red thin cat sun thread meows glows jumps."},
			{words: []string{"fat", "red", "thin", "cat", "sun", "thread", "meows", "glows", "jumps"}, capacity: 10, expected: "fat red thin cat. sun thread meows glows jumps."},
		}

		for _, test := range tests {
			p := &paragraph{capacity: test.capacity}
			if err := p.build(test.words...); err == nil {
				t.Fatal("Expected error didn't occur. Should have failed since there aren't enough words to build a paragraph with capacity ", p.capacity)
			}
		}
	})
}

func TestLoadWordBank(t *testing.T) {
	w := &wordBank{}
	if err := w.Load(fileAdjectives, fileNouns, fileVerbs); err != nil {
		t.Fatal("Unexpected error: ", err)
	}

	adjectives, err := ioutil.ReadFile(fileAdjectives)
	if err != nil {
		t.Fatal("Unexpected error: ", err)
	}
	actual := strings.Join(w.dictionary["adjectives"], ",")
	if actual != string(adjectives) {
		t.Errorf("Mismatch adjectives in dictionary.\nExpected %q\nbut got %q", adjectives, actual)
	}

	nouns, err := ioutil.ReadFile(fileNouns)
	if err != nil {
		t.Fatal("Unexpected error: ", err)
	}
	actual = strings.Join(w.dictionary["nouns"], ",")
	if actual != string(nouns) {
		t.Errorf("Mismatch nouns in dictionary.\nExpected %q\nbut got %q", nouns, actual)
	}

	verbs, err := ioutil.ReadFile(fileVerbs)
	if err != nil {
		t.Fatal("Unexpected error: ", err)
	}

	actual = strings.Join(w.dictionary["verbs"], " ")
	sanitizedVerbs := w.sanitizeVerbs(string(verbs))
	if actual != sanitizedVerbs {
		t.Errorf("Mismatch verbs in dictionary.\nExpected %q\nbut got %q", sanitizedVerbs, actual)
	}
}
