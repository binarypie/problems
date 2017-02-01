#!/usr/bin/env python3
import sys


def create_subsequence_matrix(x_string, y_string):
    matrix = [[0 for _ in range(len(y_string) + 1)] for _ in range(len(x_string) + 1)]

    for y in range(1, len(y_string) + 1):
        for x in range(1, len(x_string) + 1):
            if x_string[x-1] == y_string[y-1]:
                matrix[x][y] = matrix[x-1][y-1] + 1
            else:
                matrix[x][y] = max(matrix[x-1][y], matrix[x][y-1])

    return matrix


def trace_subsequence_matrix(matrix, x_string, y_string, x_index, y_index):
    if x_index == 0 or y_index == 0:
        return ''

    if x_string[x_index-1] == y_string[y_index-1]:
        return trace_subsequence_matrix(matrix, x_string, y_string, x_index-1, y_index-1)\
               + x_string[x_index-1]

    if matrix[x_index-1][y_index] > matrix[x_index][y_index-1]:
        return trace_subsequence_matrix(matrix, x_string, y_string, x_index-1, y_index)
    else:
        return trace_subsequence_matrix(matrix, x_string, y_string, x_index, y_index-1)


def longest_common_subsequence(filename):
    """Finds the longest, but not necessarily sequential, subsequence between two semicolon delimited
        strings on each line of the file specified by the input argument
    """

    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    pairs = []
    for line in lines:
        if line:
            line_split = line.split(';')
            if len(line_split[0]) < 51 and len(line_split[1]) < 51:
                pairs.append(line_split)

    return_list = []
    for pair in pairs:
        matrix = create_subsequence_matrix(pair[0], pair[1])
        longest_subsequence = trace_subsequence_matrix(matrix, pair[0], pair[1], len(pair[0]), len(pair[1]))

        return_list.append(longest_subsequence)

    return return_list


def main(filename):
    result = longest_common_subsequence(filename)
    print(result)


if __name__ == '__main__':
    main(sys.argv[1])
