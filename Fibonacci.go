package fibonacci

func Fibonacci(numInts int) []int64 {
	var count int
	input1 := int64(0)
	input2 := int64(1)

	return getSeq(&input1, &input2, numInts, count)
}

func getSeq(input1 *int64, input2 *int64, numInts int, count int) []int64 {
	var sequence []int64
	var retVal int64
	if (count == 0) && (numInts >= 1) {
		count++
	} else if (count == 1) && (numInts >= 2) {
		retVal = 1
		count++
	} else if count > 1 {
		count++
		retVal = *input1 + *input2
		input1 = input2
		input2 = &retVal
	}
	if numInts >= count {
		sequence = append(sequence, retVal)
		return append(sequence, getSeq(input1, &retVal, numInts, count)...)
	} else {
		return nil
	}
}
