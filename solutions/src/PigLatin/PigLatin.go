package main 

import (
    "fmt"
    "strings"
    "flag"
    "unicode"
)

const (
    vowels          string = "aeiouAEIOU"
    punctuation     string = ".?!"
    suffix          string = "ay"
    vowel_suffix    string = "way"
)

// Translate translates one or more english words into the PigLatin equlivent
func translate(orig string) string {
    var punct string
    word := orig

    // immediately return single letter
    if len(orig) == 1 {
        return orig
    }

    // if word ends in punctuation, strip and save as punct
    if strings.Contains(punctuation, orig[len(orig)-1:]) {
        punct = orig[len(orig)-1:]
        word = orig[:len(orig)-1]
    }

    // do not modify words ending in "way". keep punctuation.
    if len(word) > 2 && word[len(word)-3:] == "way" {
        return word + punct 
    }

    // apply suffix
    if strings.Contains(vowels, word[0:1]) {
        word = word + vowel_suffix + punct
    } else {
        word = word[1:] + word[0:1] + suffix + punct
    }

    // find upper case letter positions in original word
    var pos []int
    w := []rune(orig)
    for x := 0; x < len(w); x++ {
        if unicode.IsUpper(w[x]) {
            pos = append(pos, x)
        }
    }

    // apply upper case to original positions in translated
    if len(pos) > 0 {
        word = strings.ToLower(word)
        w := strings.SplitAfter(word, "")
        for x := 0; x < len(pos); x++ {
            w[pos[x]] = strings.ToUpper(w[pos[x]])
        }
        word = strings.Join(w, "")
    }
    
    return word
}

func main() {
    // arguments
    input := flag.String("input", "HeLLo World! I can't wait to explore your VAST forests. The-End!", "string to translate")
    flag.Parse()

    var output []string

    // split input by space and loop
    words := strings.Split(*input, " ")
    for _, word := range words {
        // handle hyphenated words
        if strings.Contains(word, "-") {
            w := strings.Split(word, "-")
            output = append(output, translate(w[0]) + "-" + translate(w[1]))
        } else {
            output = append(output, translate(word))
        }
    }

    fmt.Println(strings.Join(output, " "))
}
