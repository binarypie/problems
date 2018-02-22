# Library imports
import sys

# Return the Fibonacci series up to the :n-th place, as a string
def F(n):
	if n < 3:
		return ["0","1"][:n]
	else:
		seq = F(n-1)
		Fn_1 = int(seq[-1])
		Fn_2 = int(seq[-2])
		Fn = Fn_1 + Fn_2 
		return seq + [str(Fn)]

n = int(sys.argv[1])
print(', '.join(F(n)))
