#Function: Provides the Fibonocci sequence to a specific place without a loop
#Coder: David Rodriguez
#Version: 1.0
#Date of last update: 2/20/2017

def fib(i): 
   if i <= 1:
       return i
   else:
       return(fib(i-1) + fib(i-2))

ith_element = int(input("Please enter the number of generated sequences: "))
if ith_element <= 0:
   print("Plese re-run the program and enter a positive integer")
else:
   print('\nFibonacci sequence to the ' + str(ith_element) + 'th step:')
   print('Seq:  Fib:')
   for a in range(ith_element):
       print(str(a+1), ')  ' , fib(a)),
       
