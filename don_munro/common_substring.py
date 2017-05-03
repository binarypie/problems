import sys


def get_lcs(str1, str2):
    """
    Finds the longest common substring of the two provided strings.
    :param str1: string to find common substring within
    :param str2: string to find common substring within
    :return: The longest common substring.  
             If no common substring is found an empty string is returned.
    """
    if not (str1 and str2):
        return ''

    if str1 == str2:
        return str1

    rows = len(str1) + 1
    cols = len(str2) + 1
    sums = [[0 for col in range(cols)] for row in range(rows)]
    max_len = 0
    row_idx = 0
    for row in range(1, rows):
        for col in range(1, cols):
            if str1[row - 1] == str2[col - 1]:
                sums[row][col] = sums[row - 1][col - 1] + 1
                if sums[row][col] > max_len:
                    # track the length and the row index into the
                    # table where this is recorded.  We'll split
                    # an original string later with this info.
                    max_len = sums[row][col]
                    row_idx = row


    res = str1[row_idx-max_len:row_idx]
    return res


def main(argv):

    if len(argv) == 3:
        str1 = argv[1]
        str2 = argv[2]
    else:
        str1 = raw_input("String 1: ")
        str2 = raw_input("String 2: ")
    lcs = get_lcs(str1, str2)
    print lcs


if __name__ == "__main__":
    main(sys.argv)
