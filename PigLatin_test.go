package piglatin

import (
	"strings"
	"testing"
)

func TestIsConsonant(t *testing.T) {
	t.Log("Checking to see if consonants are correctly found")
	const vowels = "aeiou"
	for i := 97; i <= 122; i++ {
		if IsConsonant(byte(i)) {
			if strings.Contains(vowels, string(byte(i))) {
				t.Fail()
			}
		}
	}
}

func TestIsAlpha(t *testing.T) {

	const symbols = "[\\]`"
	for i := 85; i <= 105; i++ {
		if IsAlpha(byte(i)) {
			if strings.Contains(symbols, string(byte(i))) {
				t.Fail()
			}
		}
	}

}

func TestIsValid(t *testing.T) {

	testString := ""
	shouldPass := false
	for i := 0; i <= 5; i++ {
		switch i {
		case 0:
			testString = "anyway"
			shouldPass = false
		case 1:
			testString = "a"
			shouldPass = false
		case 2:
			testString = " "
			shouldPass = false
		case 3:
			testString = ""
			shouldPass = false
		case 4:
			testString = "tHis"
			shouldPass = true
		case 5:
			testString = "maybe"
			shouldPass = true
		}
		if IsValid(&testString) && !shouldPass {
			t.Fail()
		}
	}
}

//A REALLY simple test for checking the parsing of the words
func TestParseWords(t *testing.T) {

	testString := "Battlefront was good\nbut the Mass-Effect-series is better!"

	expected := []string{"Battlefront", " ", "was", " ", "good", "\n", "but", " ", "the", " ", "Mass", "-", "Effect", "-", "series", " ", "was", " ", "better!"}
	result := ParseWords(&testString)
	if len(result) != len(expected) {
		for i, _ := range result {
			if expected[i] != result[i] {
				t.Fail()
			}
		}
	}
}

//Another simple test to check for expected output when given a sentance.
func TestTranslate(t *testing.T) {

	testString := "HeLLo World! I can't wait to explore your VAST forests. The-End!"

	result := Translate(&testString)
	expected := "ElLOhay Orldway! I antca'y aitway otay exploreway ouryay ASTVay orestsfay. Hetay-Endway!"
	if expected != result {
		t.Fail()
	}

}

//Just another simple test to check new lines
func TestTranslateNewLines(t *testing.T) {

	testString := "Battlefront was good\nbut the Mass-Effect-series is better!"
	result := Translate(&testString)
	t.Log(result)

	expected := "Attlefrontbay asway oodgay\nutbay hetay Assmay-Effectway-eriessay isway etterbay!"

	if expected != result {
		t.Fail()
	}

}
