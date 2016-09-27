package problems

import (
	"io/ioutil"
	"os"
	"reflect"
	"testing"
)

func TestCommonSubsequence(t *testing.T) {
	var tests = []struct {
		content  []byte
		expected []string
	}{
		{content: []byte(""), expected: []string{""}},
		{content: []byte("GAC;AGCAT"), expected: []string{"AC"}},
		{content: []byte("XMJYAUZ;MZJAWXU"), expected: []string{"MJAU"}},
		{content: []byte("BANANA;ATANA"), expected: []string{"AANA"}},
		{content: []byte("GAC;AGCAT\nXMJYAUZ;MZJAWXU\n"), expected: []string{"AC", "MJAU"}},
		{content: []byte("GAC;AGCAT\nXMJYAUZ;MZJAWXU\nBANANA;ATANA\n"), expected: []string{"AC", "MJAU", "AANA"}},
		{content: []byte("GAC;AGCAT\n\nXMJYAUZ;MZJAWXU\n"), expected: []string{"AC", "MJAU"}},
		{content: []byte("\nGAC;AGCAT\n\nXMJYAUZ;MZJAWXU\n\n"), expected: []string{"AC", "MJAU"}},
	}

	for _, test := range tests {
		file, err := ioutil.TempFile("", "")
		if err != nil {
			t.Fatal("Unexpected error: ", err)
		}
		defer func() {
			if e := os.Remove(file.Name()); e != nil {
				t.Fatal("Unexpected error: ", e)
			}
		}()

		numBytes, err := file.Write(test.content)
		if err != nil {
			t.Fatalf("Unexpected error: %q. Number bytes wrote %d", err, numBytes)
		}

		allLCS, err := CommonSubsequence(file.Name())
		if err != nil {
			t.Fatal("Unexpected error: ", err)
		}

		for index, lcs := range allLCS {
			if lcs != test.expected[index] {
				t.Errorf("Mismatch LCS. Expected %q, but got %q", test.expected[index], lcs)
			}
		}
	}
}

func TestFindLongestSubsequence(t *testing.T) {
	input, expected := []byte("GAC;AGCAT"), []string{"AC"}
	actual, errs := findLongestSubsequence(input)
	if len(errs) > 0 {
		t.Fatal("Unexpected error: ", errs)
	}

	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("Mismatch longest subsequence. Bad input [%q]. Expected %q, but got %q", input, expected, actual)
	}
}

func TestComputeAll(t *testing.T) {
	var tests = []struct {
		row      string
		column   string
		expected [][]string
	}{
		{row: "", column: "", expected: nil},
		{row: "G", column: "", expected: nil},
		{row: "", column: "A", expected: nil},
		{row: "G", column: "A", expected: [][]string{[]string{""}}},
		{row: "G", column: "G", expected: [][]string{[]string{"G"}}},
		{row: "G", column: "AG", expected: [][]string{[]string{"", "G"}}},
		{row: "G", column: "AGC", expected: [][]string{[]string{"", "G", "G"}}},
		{row: "G", column: "AGCA", expected: [][]string{[]string{"", "G", "G", "G"}}},
		{row: "G", column: "AGCAT", expected: [][]string{[]string{"", "G", "G", "G", "G"}}},
		{row: "GA", column: "A", expected: [][]string{
			[]string{""},
			[]string{"A"},
		}},
		{row: "GA", column: "AG", expected: [][]string{
			[]string{"", "G"},
			[]string{"A", "A"},
		}},
		{row: "GA", column: "AGC", expected: [][]string{
			[]string{"", "G", "G"},
			[]string{"A", "A", "A"},
		}},
		{row: "GA", column: "AGCA", expected: [][]string{
			[]string{"", "G", "G", "G"},
			[]string{"A", "A", "A", "GA"},
		}},
		{row: "GA", column: "AGCAT", expected: [][]string{
			[]string{"", "G", "G", "G", "G"},
			[]string{"A", "A", "A", "GA", "GA"},
		}},
		{row: "GAC", column: "A", expected: [][]string{
			[]string{""},
			[]string{"A"},
			[]string{"A"},
		}},
		{row: "GAC", column: "AG", expected: [][]string{
			[]string{"", "G"},
			[]string{"A", "A"},
			[]string{"A", "A"},
		}},
		{row: "GAC", column: "AGC", expected: [][]string{
			[]string{"", "G", "G"},
			[]string{"A", "A", "A"},
			[]string{"A", "A", "AC"},
		}},
		{row: "GAC", column: "AGCA", expected: [][]string{
			[]string{"", "G", "G", "G"},
			[]string{"A", "A", "A", "GA"},
			[]string{"A", "A", "AC", "AC"},
		}},
		{row: "GAC", column: "AGCAT", expected: [][]string{
			[]string{"", "G", "G", "G", "G"},
			[]string{"A", "A", "A", "GA", "GA"},
			[]string{"A", "A", "AC", "AC", "AC"},
		}},
	}

	for _, test := range tests {
		actual := computeAll(test.row, test.column)
		if !reflect.DeepEqual(actual, test.expected) {
			t.Errorf("Mismatch subsequence. Bad input [%q, %q]. Expected %q, but got %q", test.row, test.column, test.expected, actual)
		}
	}
}
