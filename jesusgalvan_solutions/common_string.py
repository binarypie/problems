#!/usr/bin/python

'''
Source: git@github.com:newbootz/problems.git
Website: https://github.com/newbootz/problems
Author: Jesus Galvan (@newbootz)


# Common Strings #

Given two strings, write a program that efficiently finds the longest common subsequence.

## Example Input ##

    "Everything is awesome!"
    "Hello World is awesome!"

## Output ##

    is awesome!
'''

import sys

# Given 2 strings, find the longest common substring
def longest_common_substring(string_1, string_2):

    # Strings are the same, everything in common
    if string_1 == string_2:
        return string_1

    lcs = ''

    # Empty string has nothing in common
    if len(string_1) == 0 or len(string_2) == 0:
        return lcs

    cache = [[0] * len(string_2) for i in range(len(string_1))]

    # Iterate through the strings and fill in the matrix with lcs length
    for i in range(len(string_1)):
        for j in range(len(string_2)):
            # These characters match for these strings and respective indecies, increment the lcs counter
            if string_1[i] == string_2[j]:
                # Check if we are in the edges of matrix and is no previous lcs counter
                # Else we are not on the edges of matrix and there exists previous lcs counter to increment from
                if i == 0 or j == 0:
                    cache[i][j] = 1
                else:
                    cache[i][j] = cache[i - 1][j - 1] + 1
                
                # If we have a new lcs, save it
                if cache[i][j] > len(lcs):
                    lcs = string_1[i - cache[i][j] + 1:i + 1]
    return lcs


def main(string_1, string_2):
    result = longest_common_substring(string_1, string_2)
    print result


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

            