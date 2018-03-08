import sys

fib_memo = { 0:0 }

def fib(num):
    val = None
    
    if num in fib_memo:
        return fib_memo[num]
    
    if num < 2:
        val = num
    else:
        val = fib(num - 1) + fib(num - 2)
    
    fib_memo[num] = val
    return val
    

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Correct format is: python Fibonacci.py <no_of_places>")
        exit(1)
    
    val = int(sys.argv[1])
    if val < 1:
        print("Must be a positive integer")
        exit(1)
    
    fib(int(sys.argv[1]) - 1)
    
    print(fib_memo.values())
