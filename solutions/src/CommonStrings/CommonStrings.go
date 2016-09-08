package main

import (
    "fmt"
    "flag"
)

func find_substring(string1, string2 string) string {
    lens := make([]int, len(string1)*len(string2))
    longest := 0
    substring := ""

    for i, x := range string1 {
        for j, y := range string2 {
            if x == y {
                if i == 0 || j == 0 {
                    lens[i*len(string2)+j] = 1
                } else {
                    lens[i*len(string2)+j] = lens[(i-1)*len(string2)+j-1] + 1
                }
                if lens[i*len(string2)+j] > longest {
                    longest = lens[i*len(string2)+j]
                    substring = string1[i-longest+1 : i+1]
                }
            }
        }
    }
    return substring
}

func main() {
    string1 := flag.String("string1", "Everything is awesome!", "string 1")
    string2 := flag.String("string2", "Hello World is awesome!", "string 2")
    flag.Parse()

    fmt.Println(find_substring(*string1, *string2))
}    
