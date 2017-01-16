package main

import (
  "fmt"
  "bufio"
  "os"
  "strings"
  "bytes"
)

func main() {
  reader := bufio.NewReader(os.Stdin)
  fmt.Print("Enter string: ")
  data, err := reader.ReadString('\n')
  check(err)

  data = strings.Replace(data, "\r\n", "", -1)
  words := strings.Split(data, " ")
  max := findFrameSize(words)
  frame := initFrame(max, len(words))

  // Insert words in the previously initiailed frame
  for i := 0; i < len(words); i++ {
    frame[i+1] = frame[i+1][0:2] + words[i] + frame[i+1][1+len(words[i]):]
  }

  fmt.Println("Output:")
  for i := 0; i < len(words) + 2; i++ {
    fmt.Println(frame[i])
  }
}

// initFrame function takes the length of longest word and number of words as
// input and then constructs and returns an empty frame for that size.
func initFrame(maxWord, totalWords int) []string {
  frame := make([]string, totalWords + 2)
  var def1, def2 bytes.Buffer
  for i := 0; i < maxWord + 4;  i++ {
    def1.WriteString("*")
  }

  def2.WriteString("* ")
  for i := 0; i < maxWord - 1;  i++ {
    def2.WriteString(" ")
  }
  def2.WriteString(" *")

  for i := 0; i < totalWords + 2;  i++ {
    frame[i] = def2.String()
    if i == 0 || i == totalWords + 1 {
      frame[i] = def1.String()
    }
  }

  return frame
}

// findFrameSize function takes list of all the words as input and finds the
// size of the longest word which also is frame internal width.
func findFrameSize(words []string) int {
  max := 0
  for i := 0; i < len(words); i++ {
    if len(words[i]) > max {
      max = len(words[i])
    }
  }
  return max
}

// check if the error is present or not. If yes, panic!
func check(e error) {
  if e != nil {
    panic(e)
  }
}
