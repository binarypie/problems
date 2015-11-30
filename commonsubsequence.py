def commonsubsequence(S1,S2):
    lengths = [[0 for j in range(len(S2)+1)] for i in range(len(S1)+1)]
    # initializing 0 for row 0 and coloum 0
    for i, x in enumerate(S1):
        for j, y in enumerate(S2):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # analyzing the matrix and printing out the string
    result = ""
    x, y = len(S1), len(S2)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert S1[x-1] == S2[y-1]
            result = S1[x-1] + result
            x -= 1
            y -= 1
    return result

string1 = input("Enter your 1st String: ");
string2 = input("Enter your 2nd String: ");
finalResult = commonsubsequence(string1, string2);
print("\n commonsubsequence: " + finalResult);
