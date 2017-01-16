package main

import (
  "bytes"
  "fmt"
  "bufio"
  "os"
  "strings"
)

func main() {
  reader := bufio.NewReader(os.Stdin)
  fmt.Print("Enter string 1: ")
  string1, err1 := reader.ReadString('\n')
  check(err1)
  string1 = strings.Replace(string1, "\r\n", "", -1)

  fmt.Print("Enter string 2: ")
  string2, err2 := reader.ReadString('\n')
  check(err2)
  string2 = strings.Replace(string2, "\r\n", "", -1)

  dp := fillDpMatrix(string1, string2)
  commonSequence := getCommonSequence(dp, string1, string2);
  fmt.Printf("Common sequence is: %s", commonSequence)
}

// getCommonSequence function takes the initialized 2d matrix and both the strings
// as the input. It first finds the cell that corresponds to the common string
// with maximum length and then returns longest common string using that info.
func getCommonSequence(dp [][]int, string1, string2 string) string {
  var result bytes.Buffer
  max := 0
  indexi := 0
  indexj := 0

  // Iterate over complete matrix to find the cell that corresponds to the last
  // character of the longest common string.
  for i := 1; i <= len(string1); i++ {
    for j := 1; j <= len(string2); j++ {
      if dp[i][j] > max {
         max = dp[i][j]
         indexi = i
         indexj = j
      }
    }
  }

  // if the value of the length of longest common string is 0, return empty string.
  if max == 0 {
    return ""
  }

  // Travese the matrix diagonally to top-left starting the cell corresponding to
  // the last char of the longest common string. Build the complete string while processing
  for indexi >= 1 && indexj >= 1 && dp[indexi][indexj] >= 1 {
    result.WriteString(string(string2[indexj - 1]))
    indexi--
    indexj--
  }

  // As the string is retrieved starting from the last character of the longest common string
  // going towards first char, the actual longest string is the reverse of what was computer earlier.
  return reverseString(result.String())
}

// fillDpMatrix takes 2 strings as input. It creates and initializes a 2-d matrix
// used for finding the common string. Where row corresponds to chars in string 1
// and columns corresponds to chars in string 2. The cell in the array is updated
// accordingly if the cell corresponds to same char in both string.
func fillDpMatrix(string1, string2 string) [][]int {
  dp := make([][]int, len(string1) + 1)
  for i := 0; i < len(string1) + 1; i++ {
    dp[i] = make([]int, len(string2) + 1)
  }

  for i := 1; i <= len(string1); i++ {
    for j := 1; j <= len(string2); j++ {
      if string1[i-1] == string2[j-1] {
        dp[i][j] = dp[i-1][j-1] + 1;
      }
    }
  }

  return dp
}

// check if the error is present or not. If yes, panic
func check(e error) {
  if e != nil {
    panic(e)
  }
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
