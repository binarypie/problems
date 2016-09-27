package problems

import (
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"strings"
)

// CommonSubsequence tries to determine the longest common subsequence of the strings found in the file specified by filepath.
// Each line in the file consists of two semicolon-delimited strings, which will be read as inputs for the LCS algorithm.
// Refer https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#LCS_function_defined for the mathematical function behind this implementation.
func CommonSubsequence(filepath string) ([]string, error) {
	content, err := ioutil.ReadFile(filepath)
	if err != nil {
		log.Printf("Error while attempting to read file at %s: %s", filepath, err)
		return nil, err
	}

	lcs, errors := findLongestSubsequence(content)
	for _, e := range errors {
		err = fmt.Errorf("%s%s\n", err, e)
	}

	return lcs, err
}

func findLongestSubsequence(b []byte) ([]string, []error) {
	allLCS, errs := []string{}, []error{}
	buf := bytes.NewBuffer(b)

	var line string
	var err error
	for err != io.EOF {
		line, err = buf.ReadString('\n')
		if err != nil {
			if err != io.EOF {
				log.Printf("Error encountered while reading line %q: %s", line, err)
				errs = append(errs, err)
				continue
			}
		}

		if line == "" || line == "\n" {
			continue
		}

		splits := strings.Split(line, ";")
		all := computeAll(splits[0], splits[1])
		lcs := all[len(splits[0])-1][len(splits[1])-1]
		allLCS = append(allLCS, lcs)
	}

	return allLCS, errs
}

func computeAll(string1, string2 string) [][]string {
	if string1 == "" || string2 == "" {
		return nil
	}

	all := make([][]string, len(string1))
	for i := 0; i < len(all); i++ {
		all[i] = make([]string, len(string2))
		for j := 0; j < len(all[i]); j++ {
			all[i][j] = ""
		}
	}

	for index1, c1 := range string1 {
		for index2, c2 := range string2 {
			var i, j int
			if index1 > 0 {
				i = index1 - 1
			}
			if index2 > 0 {
				j = index2 - 1
			}

			if c1 != c2 {
				if index1 == 0 && index2 == 0 {
					continue
				}

				// in the original LCS function, if the two subsequences have the same length,
				// both will be retained. Here, we just picked one since we assume that there
				// is only one unique subsequence per string.
				var subsequence string
				if len(all[index1][j]) >= len(all[i][index2]) {
					subsequence = all[index1][j]
				} else {
					subsequence = all[i][index2]
				}

				all[index1][index2] = subsequence
			} else {
				var r string
				splits := strings.Split(all[i][j], " ")
				for _, split := range splits {
					r += split + string(c1) + " "
				}
				all[index1][index2] = strings.TrimSpace(r)
			}
		}
	}

	return all
}
