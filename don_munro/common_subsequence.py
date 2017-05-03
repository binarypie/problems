import sys

MAX_STR_LEN = 50

def _get_subsequence_table(str1, str2):
    # Define a 2d 'array' to assist with the DP solution.  We pad the 'array'
    # with an extra row/col to help clean up the logic used to calculate the
    # LCS and accept the extra space used as an accepted tradeoff
    #
    # Credit: Algorithm based on solution provided by Tushar Roy at
    #         https://www.youtube.com/watch?v=NnD96abizww
    rows = len(str1) + 1
    cols = len(str2) + 1
    sums = [[0 for col in range(cols)] for row in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            if str1[row-1] == str2[col-1]:
                sums[row][col] = sums[row-1][col-1] + 1
            else:
                # use max of element above or left
                sums[row][col] = max(sums[row-1][col], sums[row][col-1])

    return sums


def find_lcs(str1, str2):

    subseq_tbl = _get_subsequence_table(str1, str2)
    row = len(str1)
    col = len(str2)
    seq = []

    # With the subsequence tracking table in hand we now backtrack
    # to identify the characters that actually make up the LCS.
    while (row >= 0 and col >= 0):
        if subseq_tbl[row][col] == subseq_tbl[row-1][col]:
            row -=1
        elif subseq_tbl[row][col] == subseq_tbl[row][col-1]:
            col -= 1
        else:
            # Backtracking has us on the diagonal - update the LCS
            seq.insert(0, str1[row-1])
            row -= 1
            col -= 1

    return "".join(seq)



def is_valid_line(str_list):
   # For the sake of this excercise we assume that lines will be valid unless the
   # line is empty or one of the delimited strings is longer thatn MAX_STR_LEN.
   # @TDOD DMun - Consider adding more complex validation and logging
   return (len(str_list) == 2 and
           len(str_list[0]) <= MAX_STR_LEN and
           len(str_list[1]) <= MAX_STR_LEN)


def main(argv):

    if len(argv) > 1:
        filename = argv[1]
    else:
        filename = raw_input("Filename: ")

    with open(filename, 'r') as inputfile:
        for line in inputfile:
            strs = line.strip().split(';')
            if is_valid_line(strs):
                lcs = find_lcs(strs[0], strs[1])
                print ("LCS for %s and %s : %s" % (strs[0], strs[1], lcs))


if __name__ == "__main__":
    main(sys.argv)

