# call: python Fibonacci.py arg0
# param arg0 : some integer value
# Spits out the fibonacci sequence up to some input argument as a comma separated
# string. Uses dynamic programming to reduce runtime
#
# ie: python Fibonacci.py 7 -> 0, 1, 1, 2, 3, 5, 8
# Author: Jie Luo

import sys


# Recursive function that calls the calculates fibonacci numbers
# Returns the num'th fibonacci number
def fibonacci(num) :
	if fibValues[num] == None :
		fibValues[num] = fibonacci(num - 1) + fibonacci(num - 2)
	return fibValues[num]


inputVal = int(sys.argv[1])
if inputVal < 1 :
	exit();
if inputVal == 1 :
	print 0
	exit();

# Create array for values of previous additions
fibValues = [None] * inputVal
fibValues[0]= 0
fibValues[1] = 1
fibonacci(inputVal - 1)

print ', '.join(str(num) for num in fibValues)
