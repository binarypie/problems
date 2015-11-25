__author__ = 'Chenyuan'

#class Fibonacci contains two variables first and second to hold the last two numbers of the fibonacci sequence.
#It also contains two method to recursively calculate the fibonacci sequence.
class Fibonacci(object):
    #contains the last two numbers in the fibonacci sequence
    first = 0
    second = 1

    #calFibonacci is called recursively to generate the fibonacci sequence.
    #Run time complexity: big theta(N).
    #Pre-condition: num is a integer.
    #Post-condition: a fibonacci sequence starting from the third to the last positions is printed out.
    def calFibonacci(this_object, num):
        if num > 2:
            #print out one item in the fibonacci sequence
            print(",", this_object.first + this_object.second, end = "")
            #reassign the values for first and second
            temp = this_object.first
            this_object.first = this_object.second
            this_object.second = temp + this_object.second
            #reassign the number of items need to print
            num = num - 1
            #recursively call itself
            this_object.calFibonacci(num)

    #fibonacci method is where to start this program.
    #It accepts the user input of the length of fibonacci sequence.
    #Run time complexity: big theta(N)
    #Pre-condition: enough memory..
    #Post-condition: a fibonacci sequence is printed out.
    def fibonacci(this_object):
        try:
            #accept user's integer input
            num  = int(input("Please enter the length of fibonacci sequence to generate: "))
            if num == 1:
                print(0)
            elif num == 2:
                print("0, 1")
            else:
                print("0, 1", end="")
                this_object.calFibonacci(num)
        except ValueError:
            #inform user if the input type is wrong
            print("Please enter integers.And please run this program again.")


#start the program by creating an instance of the class and use the instance to call fibonacci
run = Fibonacci()
run.fibonacci()