package main

import (
    "fmt"
    "flag"
    "strings"
    "unicode/utf8"
)

func main() {
    // arguments
    input := flag.String("input", "Hello World in a frame", "string to frame")
    flag.Parse()

    // find longest word and set box width
    longest := 0
    words := strings.Split(*input, " ")
    for x := 0; x < len(words); x++ {
        length := utf8.RuneCountInString(words[x])
        if length > longest {
            longest = length 
        }
    }

    // width == longest + 4 (for right and left borders)
    width := longest+4

    // top border
    fmt.Println(strings.Repeat("*", width))    
    
    // print rows
    for x := 0; x < len(words); x++ {
        word := words[x]
        length := utf8.RuneCountInString(word)
        spaces := longest-length
        // print left border, string, fill spaces, and right border
        fmt.Println(fmt.Sprintf("* %v%v *", word, strings.Repeat(" ", spaces)))
    }

    // bottom border
    fmt.Println(strings.Repeat("*", width))
}
