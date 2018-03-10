'''
Kamran Madatov Electronic Arts

Fibonacci Solution


Code a function to generate the Fibonacci sequence to a specific place without using a loop. Recursion!
0, 1, 1, 2, 3, 5, 8, 13, 21…

Fibonacci Sequence
The Fibonacci sequence is constructed by adding the last two numbers of the sequence so far to get the next number in the sequence. The first and second numbers of the sequence are defined as 0 and 1.

Example
    Input 5
    Output 0, 1, 1, 2, 3


How to run:
Must have Python Idle Installed
Version: Python 3.6.3

1. Open terminal
2. Navigate to the file directory
3. Run on terminal: python3 fibonacci.py
4. The terminal will ask you to input the length of the fibonacci sequence, enter a number

'''

#SECOND STEP    
#Recursively will store the next fibonacci sequence to a list provided
def fibonacci(a, b,  counter, n, fibArray):
    if n == 0:              
        fibArray.pop(n)
        fibArray.pop(n)
        return fibArray
    elif n == 1:
        fibArray.pop(n)
        return fibArray
    
    if counter == n:        #end recursion
        return fibArray
    else:                   #append the next fibonacci number to a list and return
        c = a + b 
        a = b
        b = c
        fibArray.append(c)
        counter += 1
        fibArray = fibonacci (a, b, counter, n, fibArray)
        return fibArray


#FIRST STEP    
#Ask the user for the fibonacci parameter
def main():
    print ("Welcome to Fibonacci Sequence Printer")
    try:
        numFib = int(input('Enter the length of the fibonacci sequence: '))
    except:
        print("That's not an int!")
    fibArray = [0, 1] #initiate fibonacci list
    counterStart = 2
    fibSeq=fibonacci(0, 1, counterStart, numFib, fibArray)
    print(", ".join(str(num) for num in fibSeq))

#STEP ZERO
#Run main 
if __name__ == "__main__":
    main()
