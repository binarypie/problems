package problem

import "strings"

// CommonString finds the (case sensitive) common string in string1 and string2.
// If a common string exists, it returns the common string and true.
// Otherwise, it returns an empty string and false.
// This is an O(n) operation.
func CommonString(string1, string2 string) (string, bool) {
	lookup := buildLookup(string1)           // O(n)
	return findCommonString(string2, lookup) // O(n)
}

func buildLookup(s string) map[string]struct{} {
	lookup := make(map[string]struct{})
	for _, word := range strings.Split(s, " ") {
		lookup[word] = struct{}{}
	}

	return lookup
}

func findCommonString(s string, lookup map[string]struct{}) (string, bool) {
	var common string
	var found bool
	substring := s
	for index := 0; index < len(substring); {
		substring = substring[index:] // truncate the substring in every iteration
		word := findFirstWord(substring)
		if _, exist := lookup[word]; exist {
			common += " " + word
			found = true
		}

		index = len(word) + 1
	}

	return strings.TrimPrefix(common, " "), found
}

func findFirstWord(sentence string) string {
	endIndex := strings.Index(sentence, " ")
	if endIndex == -1 {
		return sentence
	}
	return sentence[:endIndex]
}
