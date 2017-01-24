import sys

memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
