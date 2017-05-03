## EA Programming Excercises by Don Munro:

All solutions assume user will be using a Python 2.7+ capable environment and that this repo 
has been cloned. 

Sample input/output are as follows:

### Common Subsequence

```
cd $YOUR_WORK_DIR/problems/don-munro
python common_subsequence.py ./subsequence.in
LCS for XMJYAUZ and MZJAWXU : MJAU
LCS for abcdef and acbef : abef
```

### Common Substring

```
cd $YOUR_WORK_DIR/problems/don-munro
python common_substring.py 'Everything is awesome!' 'Hello World is awesome!'
 is awesome!
```

Solution on hand uses a simplified version of the Common Subsequence solution.
It treats the input parameter as strings and does not take a word-by-word approach.
'''
python common_substring.py 'Everything is awesome!' 'He stared in awe!'
 awe
'''
Note that the match includes the whitespace - ' awe'

### Fibonacci Sequence
```
cd $YOUR_WORK_DIR/problems/don-munro
python fibonacci.py 8
0, 1, 1, 2, 3, 5, 8, 13
```

Limitations:
 - As it stands there is no limit on the size of a sequence that can be requested.
   While Python seems to handle precision of large values, there is an issue with
   max recurrsion depth being reached.  This is left as a know vulnerability at this
   time.
