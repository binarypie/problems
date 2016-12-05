# Thomas Doan
# Fibonacci.py
# 10/30/15
# Prints the Fibonacci sequence up to user given place

import sys

'''
Main function accepts an integer and returns the fibonacci sequence
up to that integer.
Calls auxiliary function "fib2" to print the sequence.
'''

"""
Accepts user given int amount and calls auxiliary function to print
the fibonacci sequence up to the given amount.
Args:
num: User given int amount that indicates the desired end place of the
sequence.
Returns:
An int value; the auxiliary function prints the sequence. The return value
is irrelevant in this context.
"""


def fib(num):
    return fib2(0, 1, num)


"""
Prints the fibonacci sequence up to the given end place, utilizing
the starting input of 0 and 1.
Args:
prev: The previous term in the sequence
next: The next term in the sequence; Previous term + the next term
Returns:
An int value; the auxiliary function prints the sequence. The return value
is irrelevant in this context.
"""


def fib2(prev, next, n):
    # Base case
    if n <= 1:
        return prev
    else:
        # Prints current fibonacci number
        sys.stdout.write(str(prev)+ ", ")
        return fib2(next,(prev + next), n - 1)

endPlace = input("Fibonacci sequence end place?: ")
print(fib(int(endPlace)))
