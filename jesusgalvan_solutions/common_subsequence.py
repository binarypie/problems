#!/usr/bin/python

'''
Source: git@github.com:newbootz/problems.git
Website: https://github.com/newbootz/problems
Author: Jesus Galvan (@newbootz)


# Common Subsequence
You are given two sequences. Write a program to determine the longest common subsequence between the 
two strings (each string can have a maximum length of 50 characters). NOTE: This subsequence need not be contiguous.
The input file may contain empty lines, these need to be ignored. The first argument will be a path to a filename
that contains two strings per line, semicolon delimited. You can assume that there is only one unique
subsequence per test case.

# Example Input
XMJYAUZ;MZJAWXU

# Example Output
MJAU
'''

import sys

def find_lcs(string_1, string_2):

	# Generate 2-d cache of size len(string_2)+1 x len(string_1)+1
	cache = [[0 for j in range(len(string_2)+1)] for i in range(len(string_1)+1)]

	# Generate iterables with list characters in strings and their index
	for i, x in enumerate(string_1):
		for j, y in enumerate(string_2):
			# If characters match, increment lcs counter
			if x == y:
				cache[i+1][j+1] = cache[i][j] + 1
			# If no match, take the maximum of the two previous lcs counters
			else:
				cache[i+1][j+1] = max(cache[i+1][j], cache[i][j+1])
	lcs = []
	# At this point we should have a matrix filled out with lengths of the lcs 
	# The lcs length will be at index len(string_1), len(string_2) in the matrix
	# We will traceback from there and build the lcs
	x, y = len(string_1), len(string_2)
	while (x > 0 and y > 0):
		if(cache[x][y] == cache[x-1][y]):
			x-=1
		elif(cache[x][y] == cache[x][y-1]):
			y-=1
		else:
			lcs = [string_1[x-1]] + lcs
			x-=1
			y-=1
	return ''.join(lcs)

def longest_common_subsequence(filename):
	# Parse the lines of this file
	#try block...also strip lines of whitespaceS..check if delimrter
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    pairs = []
    # Delimeter is semicolon for the two strings, they can't be larger than 50 length
    for line in lines:
        if line:
            line_split = line.split(';')
            if len(line_split[0]) <= 50 and len(line_split[1]) <= 50:
                pairs.append(line_split)

    return_list = []
    # Find the lcs for each of the pairs
    for pair in pairs:
        longest_subsequence = find_lcs(pair[0], pair[1])
        return_list.append(longest_subsequence)

    return return_list

def main(filename):
    result = longest_common_subsequence(filename)
    print result


if __name__ == '__main__':
    main(sys.argv[1])