var x = prompt("Enter a number to generate the Fibonacci sequence: ");
var str = "";
function Fibonacci(x) { //recursive function 
if (x == 0) 
  return 0;
if (x == 1 || x == 2) //0, 1 are base case 
  return 1;

  return Fibonacci(x-1) + Fibonacci(x-2);
}

for (var i=0; i<x; i++) { //loop to output
  str += Fibonacci(i) +", ";  
}

// 0 1 1 2 3 5 
//
// input: 5
// fib(4) + fib(3)
// fib(3) + fib(2)      fib(2) + fib(1)
// fib(2) + fib(1) + 1      1 + 1
// 1 + 1 + 1 +
//
//= 5
console.log(str);

