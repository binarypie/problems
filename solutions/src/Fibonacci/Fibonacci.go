package main

import (
    "fmt"
    "flag"
    "bytes"
)

// return a function that returns successive
// numbers in the sequence
func fibonacci() func() int {
    x, y := 0, 1
    return func() (sequence int) {
        sequence, x, y = x, y, x+y
        return 
    }
}

func main() {
    // arguments
    position := flag.Int("position", 5, "print sequence up to position")
    flag.Parse()
        
    // start our sequence
    fib := fibonacci()

    // build output buffer and create sequence up to position
    var seq bytes.Buffer
    for i := 0; i < *position; i++ {
        // comma delimit
        if i == *position-1 {
            seq.WriteString(fmt.Sprintf("%v", fib()))
        } else {
            seq.WriteString(fmt.Sprintf("%v, ", fib()))
        }
    }
    fmt.Println(seq.String())
}
