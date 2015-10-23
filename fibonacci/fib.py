'''
Daniel Edwards
10/22/2015
fib.py
A program that generates and prints the fibonacci sequence.
'''
import sys #importing so I can print without new lines or spaces

'''
The following function accounts for edge cases of wanting 0 or 1 fibonacci
numbers. It then prints the first number, 0, before calling the recursive
fib function.
@param aTotal The desired place in the Fibonacci sequence to end at.
'''
def fibonacci(aTotal):
    if(aTotal <= 0):
        return
    elif(aTotal == 1):
        sys.stdout.write(str(0)),
    elif(aTotal > 1):
        sys.stdout.write(str(0)),
        fib(0, 1, 2, aTotal)

'''
The following function prints the current value, compares the current location
in the sequence to the desired endpoint and recurs if it has not reached
the endpoint.
@param aLast The previous number in the sequence
@param aCurrent The current number in the sequence
@param aIndex The current position in the sequence
@param aTotal The desired endpoint in the sequence
'''
def fib(aLast, aCurrent, aIndex, aTotal):
    sys.stdout.write(", " + str(aCurrent)),
    if(aIndex < aTotal):
        fib(aCurrent, aCurrent + aLast, aIndex + 1, aTotal)

tInput = input("Sequence endpoint: ")
fibonacci(tInput)
