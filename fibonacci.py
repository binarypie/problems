"""
Krishna Chaitanya Kandula
"""

out_of_bounds_error = "index must be greater than or equal to 0"


def fibonacci_recursive(index):
    """Calculate the fibonacci number at a given index using recursion.
    This way of calculating the fibonacci number is done without
    any kind of memoization/dynamic programming and hence the
    runtime is in the order of O(2^n). This is because there are 2
    branching calls each time an index needs to be calculated.

    :param index: the index in the sequence
    :return: the fibonacci number at the index
    """
    # Error check index bounds
    if index < 0:
        raise ValueError(out_of_bounds_error)

    # Base case
    if index == 0 or index == 1:
        return index
    return fibonacci_recursive(index - 1) + fibonacci_recursive(index - 2)


def fibonacci_memoized(index):
    """Calculate the fibonacci number at a given index using recursion and memoization.
    This method of calculating a fibonacci number is done using memoization
    which trades time complexity for a little bit more space complexity. Previous
    answers are stored in an array which can then be reused. The time complexity is
    reduced to O(n), and the space complexity also becomes O(n).

    :param index: the index in the sequence
    :return: the fibonacci number at the index
    """
    # Error check index bounds
    if index < 0:
        raise ValueError(out_of_bounds_error)
    return fibonacci_memoized_helper(index, [0, 1])


def fibonacci_memoized_helper(index, memo):
    if len(memo) <= index:
        memo.append(fibonacci_memoized_helper(index - 1, memo) + fibonacci_memoized_helper(index - 2, memo))
    return memo[index]


if __name__ == '__main__':
    print(fibonacci_recursive(10))
    print(fibonacci_memoized(10))
