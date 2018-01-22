# Eric Chien's Solution for EA Coding Assignment 

## Installation

Please make sure you have Python 2.7+ installed on your machine.

Next, clone this repository to your machine with the follow script

```
git clone https://github.com/virtuositeit/problems.git
```

Once you have the repository cloned, you can proceed to navigate to the 'problems' folder


## Solution for Fibonacci

Please run the python program with the following script:

```
python Solution_Fibonacci.py
```

The program will prompt for hte number of Fabonacci numbers to generate. Since no modification is done to Python's recursion depth limit, the largest fibonacci number the program can generate is the 999th fibonacci number.


## Solution for Pig Latin

Please run the python program with the following script:

```
python Solution_PigLatin.py
```

The program will print out a default set of test strings translated into Pig Latin.


## Solution for Essay Monkey

Please run the python program with the following script:

(solution 1, the algorithm reads chars one by one, should be more memory efficient)
```
python Solution_EssayMonkey_method1.py
```

(solution 2, the algorithm uses split, which is less memory efficient)
```
python Solution_EssayMonkey_method2.py
```

The program will then prompt for integer inputs as the number of paragraphs and sentences per paragraph to generate. Each sentence will not have the same length (which is what I perceive to be the requirement of the problem.)
