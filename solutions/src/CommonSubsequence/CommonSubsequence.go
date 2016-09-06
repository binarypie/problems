package main

import (
    "fmt"
    "flag"
    "bufio"
    "os"
    "bytes"
    "strings"
)

func subsequence(a, b string) string {
    // build sequence table grid
    a_slice, b_slice := []rune(a), []rune(b)
    a_len, b_len := len(a_slice), len(b_slice)
    lengths := make([][]int, a_len+1)
    for x := 0; x <= a_len; x++ {
        lengths[x] = make([]int, b_len+1)
    }

    // map path through table grid
    for x := 0; x < a_len; x++ {
        for y := 0; y < b_len; y++ {
            if a_slice[x] == b_slice[y] {
                lengths[x+1][y+1] = lengths[x][y] + 1
            } else if lengths[x+1][y] > lengths[x][y+1] {
                lengths[x+1][y+1] = lengths[x+1][y]
            } else {
                lengths[x+1][y+1] = lengths[x][y+1]
            }
        }
    }

    // traceback through table and read substring
    sstring := make([]rune, 0, lengths[a_len][b_len])
    for x, y := a_len, b_len; x != 0 && y != 0; {
        if lengths[x][y] == lengths[x-1][y] {
            x--
        } else if lengths[x][y] == lengths[x][y-1] {
            y--
        } else {
            sstring = append(sstring, a_slice[x-1])
            x--
            y--
        }
    }
    // reverse the substring and return
    for i, j := 0, len(sstring)-1; i < j; i, j = i+1, j-1 {
        sstring[i], sstring[j] = sstring[j], sstring[i]
    }
    return string(sstring)
}

func main() {
    // arguments
    string_file := flag.String("file", "CommonSubsequence.txt", "strings file")
    flag.Parse()

    // open file
    file, error := os.Open(string(*string_file))
    if error != nil {
        fmt.Fprintf(os.Stderr, "%v\n", error)
        os.Exit(1)
    }
    defer file.Close()

    // start scanner
    s := bufio.NewScanner(file)
    line := 0 // keep track of line number in case of error
    for s.Scan() {
        line++
        
        // ignore blank lines
        if len(bytes.TrimSpace(s.Bytes())) == 0 {
            continue
        }
        parts := strings.Split(s.Text(), ";")

        // print subsequence if within character limits
        if len(parts[0]) <= 50 && len(parts[1]) <= 50 {
            fmt.Printf("%v\n", subsequence(parts[0], parts[1])) 
        } else {
            fmt.Fprintf(os.Stderr, "%v:%v 50 char limit\n", os.Args[1], line)
            os.Exit(1)
        }
    }
}
