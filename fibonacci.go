package main

import "fmt"

var n int

func main() {
   fmt.Print("Enter n:")
   fmt.Scanf("%d", &n)
   printFibonacci(0)
}

func printFibonacci(curr int){
	fmt.Print(fibonacci(curr))
	if(curr<n-1){
		fmt.Print(",")
	}
	if(curr<n-1){
		printFibonacci(curr+1)
	}
}

func fibonacci(curr int)int{
	if(curr==0 || curr==1){
		return curr
	}else{
		return fibonacci(curr-1)+fibonacci(curr-2)
	}
}