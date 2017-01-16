package main

import (
	"fmt"
)

// adding memoization so that the results of previous fibonacci series can be
// stored and used for generating new series if any (if later program is to be changed)
var FIB_MEM = make(map[uint64]string)

func main() {
	var limit uint64
	fmt.Printf("Enter the number of elements required in the fibonacci series: ")
	_, err := fmt.Scanf("%d", &limit)

	// panic if there is error scanning from STDIN
	check(err)

	// panic if limit provided is less than zero
	if limit < 0 {
		panic("Number of elements cannot be less than 0!!")
	}

	output := getFibonacciSeriesStr(limit)

	fmt.Println(output)
}


func getFibonacciSeriesStr(limit uint64) string {
	// if limit is equal to zero return immediately
	if limit == 0 {
		return ""
	}

	op := "Required fibonacci series is: 0"
	if limit >= 2 {
		op = fmt.Sprintf("%s, 1", op)
	}

	return generateFibonacciSeries(0, 1, limit-2, op)
}

// generateFibonacciSeries generates fibonacci series till a limit recursively while memoizing intermediate
// series steps
func generateFibonacciSeries(prev1 uint64, prev2 uint64, limit uint64, op string) string {
	if limit <= 0 {
		return op
	}

	var respStr string
	val, hasKey := FIB_MEM[limit]

	if hasKey {
		respStr = val
	} else {
		respStr = generateFibonacciSeries(prev2, prev1+prev2, limit-1, fmt.Sprintf("%s, %d", op, prev1+prev2))
		FIB_MEM[limit] = respStr
	}

	return respStr
}

// check if the error is present or not. If yes, panic!
func check(e error) {
	if e != nil {
		panic(e)
	}
}
