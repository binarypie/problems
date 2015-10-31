import sys

__author__ = 'joanhong'


# place to generate fibonacci number to
def fibonacci(place):
    previous = list([0]*(place+1))
    return fibonacci_helper(place, previous)


# helper handles recursion, store values in 'previous' array
def fibonacci_helper(n, previous):
    if n == 0:
        sys.stdout.write(str(n))
    elif n == 1:
        # make sure only one call for n ==1 is printed
        if previous[n] == 0:
            previous[n] = 1
        else:
            sys.stdout.write(", "+str(n))
    elif previous[n] == 0:
        previous[n] = fibonacci_helper(n-1, previous) + fibonacci_helper(n-2, previous)
        sys.stdout.write(", "+str(previous[n]))
    return previous[n]


if __name__=="__main__":
    running = True
    while(running):
        user_input = raw_input("Enter in specific place to generate Fibonacci sequence to:")

        # check for invalid input
        if not str.isdigit(user_input):
            sys.stdout.write("Please enter a valid place\n")
        elif int(user_input) < 1:
            sys.stdout.write("Please enter a valid place\n")
        # valid input, run fibonacci
        else:
            user_input = int(user_input)
            fibonacci(user_input-1)
            running = False
