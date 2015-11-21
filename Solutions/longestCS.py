import sys

def lcs(str_a , str_b):
    
    """
    Find the Longest common subsequence in the given two strings
    Dynamic Programming 
    
    """
    m = len(str_a)
    n = len(str_b)
    match = [[None]*(n+1) for i in xrange(m+1)]
	
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                match[i][j] = 0
            elif str_a[i-1] == str_b[j-1]:
                match[i][j] = match[i-1][j-1]+1
            else:
                match[i][j] = max(match[i-1][j] , match[i][j-1])
    
    """
    Now traverse back to reconstruct the lcs
    
    """
    len_a, len_b = len(str_a), len(str_b)
    result = ""
    
    while len_a != 0 and len_b != 0:
        if match[len_a][len_b] == match[len_a-1][len_b]:
            len_a -= 1
        elif match[len_a][len_b] == match[len_a][len_b-1]:
            len_b -= 1
        else:
            if str_a[len_a-1] == str_b[len_b-1]:
				result = str_a[len_a-1]+result
				len_a -= 1
				len_b -= 1
   
    return result

if __name__ == "__main__":
    print "Usage: longestCS.py <path/to/inputFile>"
    
    file = open(sys.argv[1], 'r')
    for line in file:
        input = line.strip().split(';')
        print lcs(input[0], input[1])
    