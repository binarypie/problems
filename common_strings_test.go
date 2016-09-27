package problems

import "testing"

func TestCommonString(t *testing.T) {
	var tests = []struct {
		input1   string
		input2   string
		expected string
		found    bool
	}{
		// test cases for common strings
		{input1: "Test", input2: "Test", expected: "Test", found: true},
		{input1: "Test ", input2: "Test", expected: "Test", found: true},
		{input1: " Test", input2: "Test", expected: "Test", found: true},
		{input1: " Test ", input2: "Test", expected: "Test", found: true},
		{input1: "My test", input2: "test", expected: "test", found: true},
		{input1: "test", input2: "My test", expected: "test", found: true},
		{input1: "Everything awesome!", input2: "Hello is awesome!", expected: "awesome!", found: true},
		{input1: "Hello is awesome!", input2: "Everything awesome!", expected: "awesome!", found: true},
		{input1: "is awesome!", input2: "is awesome", expected: "is", found: true},
		{input1: "is awesome!", input2: "is awesome!", expected: "is awesome!", found: true},
		{input1: "Everything is awesome!", input2: "Hello is awesome!", expected: "is awesome!", found: true},

		// test cases for no common strings
		{input1: "", input2: "", expected: "", found: false},
		{input1: "Test", input2: "", expected: "", found: false},
		{input1: "", input2: "Test", expected: "", found: false},
		{input1: "Everything", input2: "Hello", expected: "", found: false},
		{input1: "is awesome", input2: "awesome!", expected: "", found: false},

		// test cases for case sensitivity
		{input1: "Is Awesome", input2: "is awesome", expected: "", found: false},
		{input1: "IS AWESOME", input2: "is awesome", expected: "", found: false},
		{input1: "is awesome", input2: "IS AWESOME", expected: "", found: false},
		{input1: "is awesome !!", input2: "IS awesome !!", expected: "awesome !!", found: true},
	}

	for _, test := range tests {
		actual, found := CommonString(test.input1, test.input2)
		if test.found != found {
			t.Errorf("Mismatch found value. Bad inputs [%q,%q]. Expected %t, but got %t", test.input1, test.input2, test.found, found)
		}
		if test.expected != actual {
			t.Errorf("Mismatch subsequence. Bad inputs [%q,%q]. Expected %q, but got %q", test.input1, test.input2, test.expected, actual)
		}
	}
}
