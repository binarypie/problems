maxval = int(raw_input())
ans = []

# Recursively add fibonacci numbers up to maxval
def fib(a=0, b=1, count=0):
    if count < maxval:
        ans.append(str(a))
        fib(a + b, a, count + 1)

fib()
print (', '.join(ans))