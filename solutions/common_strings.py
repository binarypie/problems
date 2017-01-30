#!/usr/bin/env python3
import sys


def longest_common_string(first_str, second_str):
    """Finds the first, longest match between the two input strings, where 'first' is relative to the
        smaller string.
    """

    if first_str == "" or second_str == "":
        return ""

    if first_str == second_str:
        return first_str

    longest, shortest = first_str, second_str
    if len(longest) < len(shortest):
        longest, shortest = shortest, longest

    if shortest in longest:
        return shortest

    longest_substring = ""
    short_length = len(shortest)
    start_index = 0
    end_index = 1

    while end_index <= short_length:
        window = shortest[start_index:end_index]
        if window in longest:
            longest_substring = window
            end_index += 1
        else:
            start_index += 1
            end_index += 1

    return longest_substring


def main(first_string, second_string):
    result = longest_common_string(first_string, second_string)
    print(result)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
