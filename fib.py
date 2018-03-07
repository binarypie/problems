import sys

if (len(sys.argv) != 2):
    print "Incorrect number of arguments. \n Usage: fib.py <integer>"
    exit(1)

a = 0
b = 1
count = 0
value = int(sys.argv[1])
res = []

# fib numbers up to value, recursively
def fib(a, b, count):
	if count < value:
		res.append(str(a))
		fib(a + b, a, count + 1)

fib(a, b, count)
print ', '.join(res)
