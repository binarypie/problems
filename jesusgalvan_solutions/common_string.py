#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def longest_common_substring(string_1, string_2):

    # Strings are the same
    if string_1 == string_2:
        return string_1

    lcs = ''

    # Empty string has nothing in common
    if len(string_1) == 0 or len(string_2) == 0:
        return lcs

    # 2-d array cache of size len(string_2)xlen(string_1)
    cache = [[0] * len(string_2) for i in range(len(string_1))]

    # Iterate through the strings and fill in the matrix with lcs length
    for i in range(len(string_1)):
        for j in range(len(string_2)):
            # These characters match at these repsective strings and indicies, increment the lcs counter
            if string_1[i] == string_2[j]:
                # Case where we are in the edges of matrix and is no previous lcs counter
                if i == 0 or j == 0:
                    cache[i][j] = 1
                # Case where we are not on the edges of matrix and there exists previous lcs counter to increment from
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

            