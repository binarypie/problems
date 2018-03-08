import sys

def fib_list(x):
    """Returns list of the first x Fibonacci numbers"""
    result_list = [-1] * x

    def fib(index):
        """Returns the Fibonacci number at index
        and adds the fibonacci number to the list
        """
        result = 0
        if index == 2:
            result = 1
        elif index > 2:
            result = fib(index - 1) + fib(index - 2)
        if result_list[index-1] == -1:
            result_list[index-1] = result
        return result

    if x > 0:
        fib(x)
    else:
        sys.exit("Fibonacci requires an integer greater than 0.")
    return result_list


if len(sys.argv) == 2:
    try:
        index = int(sys.argv[1])
    except:
        sys.exit("Command line argument must be an integer")
    print(fib_list(index))
else:
    sys.exit("Fibonacci requires one integer")
