package main

import (
	"fmt"
	"strconv"
)

const MAX_NUMBER = 93

func main() {
	numInts := getInput()
	var count int
	input1 := int64(0)
	input2 := int64(1)

	//Check for initial cases.
	if numInts >= 1 {
		count++
		fmt.Printf("%d, ", 0)
	}
	if numInts >= 2 {
		count++
		fmt.Printf("%d, ", 1)
	}
	fibonacci(&input1, &input2, numInts, &count)
}

func getInput() int {
	// Any above 93, and longs start to wrap around to the negatives.
	fmt.Println("Please input the number of fibonacci numbers you want: (0-93)")
	var input string
	fmt.Scanln(&input)
	numInts, err := strconv.ParseInt(input, 10, 32)
	if err != nil {
		fmt.Println("Could not parse int, try again!\n" + err.Error())
		return getInput()
	} else if numInts > MAX_NUMBER {
		fmt.Println("Number too large, try again!\n")
		return getInput()
	} else if numInts < 0 {
		fmt.Println("Number must be positive, try again!\n")
		return getInput()
	}
	return int(numInts)
}

func fibonacci(input1 *int64, input2 *int64, numInts int, count *int) {
	if numInts > *count {
		*count++
		retVal := *input1 + *input2
		input1 = input2
		input2 = &retVal
		fmt.Printf("%d, ", retVal)
		fibonacci(input1, &retVal, numInts, count)
	} else {
		fmt.Printf("\b\b\n")
	}
}
