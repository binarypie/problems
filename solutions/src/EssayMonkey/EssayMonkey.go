package main

import (
    "fmt"
    "flag"
    "math/rand"
    "strings"
    "bytes"
    "io/ioutil"
    "os"
)

func main() {
    // arguments
    noun_file := flag.String("nouns", "EssayMonkeyNouns.txt", "nouns filename")
    verb_file := flag.String("verbs", "EssayMonkeyVerbs.txt", "verbs filename")
    adjective_file := flag.String("adjectives", "EssayMonkeyAdjectives.txt", "adjectives filename")
    num_paragraphs := flag.Int("paragraphs", 5, "number of paragraphs")
    num_sentences := flag.Int("sentences", 15, "sentences per paragraph")
    flag.Parse()

    // read word lists from input files
    nouns_l, error := ioutil.ReadFile(*noun_file)
    if error != nil {
        fmt.Fprintf(os.Stderr, "%v\n", error)
        os.Exit(1)
    }

    verbs_l, error := ioutil.ReadFile(*verb_file)
    if error != nil {
        fmt.Fprintf(os.Stderr, "%v\n", error)
        os.Exit(1)
    }

    adjectives_l, error := ioutil.ReadFile(*adjective_file)
    if error != nil {
        fmt.Fprintf(os.Stderr, "%v\n", error)
        os.Exit(1)
    }

    // split comma delimited lists into slices
    var nouns []string = strings.Split(string(nouns_l), ",")
    var verbs []string = strings.Split(string(verbs_l), ",")
    var adjectives []string = strings.Split(string(adjectives_l), ",")

    // start building our essay
    for i := 0; i < *num_paragraphs; i++ {
        var paragraph bytes.Buffer
        for i := 0; i < *num_sentences; i++ {

            // randomize two sentence lengths inside each paragraph
            rand_length := rand.Intn(2)
            switch rand_length {
    
            case 0:
                // clean up white space and write sentence to paragraph buffer
                adj := strings.TrimSpace(adjectives[rand.Intn(len(adjectives))])
                noun := strings.TrimSpace(nouns[rand.Intn(len(nouns))])
                verb := strings.TrimSpace(verbs[rand.Intn(len(verbs))])
                paragraph.WriteString(fmt.Sprintf("The %v %v %v. ", 
                    adj, noun, verb))

            case 1:
                // clean up white space and write sentence to paragraph buffer
                adj1 := strings.TrimSpace(adjectives[rand.Intn(len(adjectives))])
                adj2 := strings.TrimSpace(adjectives[rand.Intn(len(adjectives))])
                noun1 := strings.TrimSpace(nouns[rand.Intn(len(nouns))])
                noun2 := strings.TrimSpace(nouns[rand.Intn(len(nouns))])
                verb := strings.TrimSpace(verbs[rand.Intn(len(verbs))])
                paragraph.WriteString(fmt.Sprintf("The %v %v %v the %v %v. ", 
                    adj1, noun1, verb, adj2, noun2))

            }

        }
        // print paragraph
        fmt.Printf("%v\n\n", paragraph.String())
    }
}
