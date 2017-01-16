package main

import(
  "strings"
  "fmt"
  "regexp"
  "bytes"
  "bufio"
  "os"
)

// struct to hold data related to punctuation and its position from end of the word
type puctuationRecord struct {
  punctuation string
  positionFromEnd int
}

const (
  vowels                  string = "aeiouAEIOU"
  vowelWordsSuffix        string = "way"
  consonantWordsSuffix    string = "ay"
  splitRegex              string = "[ -]"
  punctuationRegex        string = "[;:,_.?!\\(\\)\\[\\]\\{\\}'\"]"
  testString              string = "HeLLo World! I can't wait to explore your VAST forests. The-End!"
)

func main(){
  var result, token bytes.Buffer

  fmt.Printf("Enter the string to be transformed: ")
  reader := bufio.NewReader(os.Stdin)
  input, err := reader.ReadString('\n')
  check(err)

  input = strings.Replace(input, "\r\n", "", -1)

  // Input is processed as one token at a time where tokens are space or hyphen
  // separated. The extracted token is first analyzed to get a token without punctuation
  // and its relevant punctuationRecord. It is then pig latinized and finally the
  // punctuations are added back to modified token.
  for i := 0; i < len(input); i++ {
    char := string(input[i])
    switch {
      case char == " " || char == "-" || i == len(input) - 1:
        if len(token.String()) > 0 {
          tok, puncData := getTokenDetails(token.String())
          pigToken := pigLatinize(tok)
          pigToken = addPunctuations(pigToken, puncData)
          result.WriteString(pigToken)
          token.Reset()
        }
        result.WriteString(char)
      default:
        token.WriteString(char)
    }
  }

  fmt.Printf("\nOutput:\n%s", result.String())
}

// pigLatinize function takes token as an input and converts it to pig-latin
// form. If the token is consisting of single character or ending with 'way',
// then it is returned as it is. If token starts with vowel, then token + 'way'
// is returned as the output. Otherwise, it is handled by doing one character
// circular rotation while preserving char case.
func pigLatinize(token string) string {
  vowelStartRegex := regexp.MustCompile("^["+ vowels +"].*$")
  vowelWordsSuffixRegex := regexp.MustCompile("^.*" + vowelWordsSuffix + punctuationRegex +"*$")
  switch {
    case len(token) == 1 || vowelWordsSuffixRegex.MatchString(token):
      return token
    case vowelStartRegex.MatchString(token):
      return token + vowelWordsSuffix
    default:
      // This is the case for all the tokens begining with consonants
      return processConsonantStartWords(token) + consonantWordsSuffix
  }
}

// processConsonantStartWords function takes token as input and it performs one
// character circular rotation while preserving char case.
func processConsonantStartWords(token string) string {
  var tok bytes.Buffer
  var final string
  first := string(token[0])

  for i := 1; i <= len(token); i++ {
    prev := string(token[i-1])
    current := first
    if i < len(token) {
      current = string(token[i])
    }
    final = strings.ToLower(current)
    if prev == strings.ToUpper(prev) {
      final = strings.ToUpper(current)
    }

    tok.WriteString(final)
  }

  return tok.String()
}

// addPunctuations function takes pigLatinized token and punctuationRecords
// and then adds the punctions at the required locations (calculated from end)
func addPunctuations(token string, puncData []puctuationRecord) string {
  for i := 0; i < len(puncData); i++ {
    punc := puncData[i]
    token = token[:len(token) - punc.positionFromEnd] + punc.punctuation + token[len(token) - punc.positionFromEnd:]
  }
  return token
}

// getTokenDetails takes token as input and returns a modified token without any
// punctuations and an array of punctuationRecord that holds the type of
// punctuation and its location from the end of the word. This information
// is used later to add the punctions back in the word at correct location.
func getTokenDetails(token string) (string, []puctuationRecord) {
  punctuationData := make([]puctuationRecord, len(token))
  puncRegexMatcher := regexp.MustCompile(punctuationRegex)
  var tok bytes.Buffer

  for i := len(token) - 1; i >=0 ; i-- {
    char := string(token[i])
    switch {
      case puncRegexMatcher.MatchString(char):
        punctuationData = append(punctuationData, puctuationRecord{char, len(token) - 1 - i})
      default:
        tok.WriteString(char)
    }
  }

  return reverseString(tok.String()), punctuationData
}

// function to reverse the string passed as an argument
func reverseString(token string) string {
  var tok bytes.Buffer
  for i := len(token) - 1; i >=0 ; i-- {
    char := string(token[i])
    tok.WriteString(char)
  }
  return tok.String()
}

// check if the error is present or not. If yes, panic
func check(e error) {
  if e != nil {
    panic(e)
  }
}
