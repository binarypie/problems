package main

import (
        "bufio"
        "bytes"
        "fmt"
        "os"
        "regexp"
        "strings"
)

const (
        validCaseRegex string = "^.+;.+$"
)

func main() {
        reader := bufio.NewReader(os.Stdin)
        fmt.Print("Enter file path: ")
        filePath, err1 := reader.ReadString('\n')
        check(err1)
        filePath = strings.Replace(filePath, "\r\n", "", -1)

        file, err2 := os.Open(filePath)
        check(err2)
        defer file.Close()

        matcher := regexp.MustCompile(validCaseRegex)
        scanner := bufio.NewScanner(file)
        for scanner.Scan() {
                switch {
                case matcher.MatchString(scanner.Text()):
                        data := strings.Split(strings.Replace(scanner.Text(), "\r\n", "", -1), ";")
                        dp := fillDpMatrix(data[0], data[1])
                        commonSubsequence := getCommonSubsequence(dp, data[0], data[1])
                        fmt.Println("\nInput line: ", scanner.Text())
                        fmt.Printf("Common Subsequence is: %s\n", commonSubsequence)
                default:
                        fmt.Println("\nSkipped input line: " + scanner.Text() + ". Not matching pattern: " + validCaseRegex)
                }
        }
}

// getCommonSubsequence function takes the initialized 2d matrix and both the strings
// as the input. It returns longest common subsequence using that info.
func getCommonSubsequence(dp [][]int, string1, string2 string) string {
        var result bytes.Buffer

        // start from bottom-right cell which will have the length of the
        // longest common subsequence
        i := len(string1)
        j := len(string2)
        for i >= 1 && j >= 1 {
                if dp[i][j] != dp[i-1][j] && dp[i][j] != dp[i][j-1] {
                        i--
                        j--
                        result.WriteString(string(string2[j]))
                } else if dp[i][j] == dp[i-1][j] {
                        i--
                } else {
                        j--
                }
        }

        // As the string is retrieved starting from the last character of the longest common subsequence
        // going towards first char, the actual longest string is the reverse of what was computer earlier.
        return reverseString(result.String())
}

// fillDpMatrix takes 2 strings as input. It creates and initializes a 2-d matrix
// used for finding the common subsequence. Where row corresponds to chars in string 1
// and columns corresponds to chars in string 2. The cell in the array is updated
// accordingly if the cell corresponds to same char in both string.
func fillDpMatrix(string1, string2 string) [][]int {
        dp := make([][]int, len(string1)+1)
        for i := 0; i < len(string1)+1; i++ {
                dp[i] = make([]int, len(string2)+1)
        }

        for i := 1; i <= len(string1); i++ {
                for j := 1; j <= len(string2); j++ {
                        if string1[i-1] == string2[j-1] {
                                dp[i][j] = dp[i-1][j-1] + 1
                        } else {
                                dp[i][j] = dp[i-1][j]
                                if dp[i][j-1] > dp[i][j] {
                                        dp[i][j] = dp[i][j-1]
                                }
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
        for i := len(token) - 1; i >= 0; i-- {
                char := string(token[i])
                tok.WriteString(char)
        }
        return tok.String()
}
