def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

nterms = int(input("How many terms? "))
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("\nFibonacci sequence:")
   for i in range(nterms):
       print(fibonacci(i)),
