import sys

"""Fibonacci Generator 

The Fibonacci sequence is constructed by adding the last two numbers of the sequence so far to 
get the next number in the sequence. The first and second numbers of the sequence are
defined as 0 and 1.

    EG: 0, 1, 1, 2, 3, 5, 8, 13, 21
    
The generator avoids the use of a loop and instead provides a recursive solution to form 
the sequence.   

## Example Input ##

    5

## Example Output ##

    0, 1, 1, 2, 3

Ref: https://github.com/binarypie/problems/blob/master/Fibonacci.md

"""
class FibonacciGenerator():

    def __init__(self):
        # Track a generated sequence at the class level.  We'll extend this
        # list as the sequence is created and use previously calculated
        # values as a means of minimizing recursive calls.
        self.sequence = [0, 1]

    def generate_sequence(self, length):
        def gen_fib_helper(seq_idx):

            if len(self.sequence) > seq_idx:
                return self.sequence[seq_idx]

            # Use fib(n) = fib(n - 2) + fib(n - 1) to ensure that we work from
            # low index to high as the sequence is built out.
            fib_num = gen_fib_helper(seq_idx - 2) + gen_fib_helper(seq_idx - 1)
            self.sequence.append(fib_num)
            return fib_num

        gen_fib_helper(length - 1)
        print(self.sequence)


def main(argv):

    if len(argv) > 1:
        seq_length = argv[1]
    else:
        seq_length = raw_input("Sequence length: ")

    generator = FibonacciGenerator()
    generator.generate_sequence(int(seq_length))
    print(generator.sequence)

if __name__ == "__main__":
    main(sys.argv)



