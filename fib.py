import sys

def fib(n, dp):
    if n is 0 or n is 1:
        return n
    if dp[n-1] != 0:
        return dp[n-1]
    f = fib(n-1, dp)+fib(n-2, dp)
    dp[n-1] = f
    return f

if __name__=="__main__":
    print("Enter n:")
    n = int(sys.stdin.readline())
    dp = [0] * n # array to save intermediate results
    dp[0] = 0
    dp[1] = 1
    print(fib(n, dp))
