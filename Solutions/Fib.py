
#calulctes the fibonacci number

fib = {}
fib[0] =0
fib[1]=1

def func(n):
    """ Caluclates the finbonacci number using using store and compute """
    if n not in fib:
        fib[n] = func(n-1) + func(n-2)
    return fib[n]
    

if __name__ == "__main__":
    print "Fibonacci sequence generator...."
    num = int(raw_input("enter number : "))
    if (num<0):
        print "Enter positive number"
    else:
        for i in range(0,num):
            print func(i),