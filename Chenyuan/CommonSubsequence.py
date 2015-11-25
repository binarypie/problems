__author__ = 'Chenyuan'

#class LCS contains two methods: readFile and lcs.
#readFile is a internal method called by lcs.
#lcs is used to find the longest common sub-sequence.
class LCS(object):
    #read and process the file
    #Run time complexity: big theta(N)
    #N is the number of lines in the file
    #Pre-condition: the file contains either two strings per line, semicolon delimited, or empty line.
    #Post-condition: return a list of sequence pairs
    def readFile(this_object, fname):
        file = list()
        with open(fname) as f:
            #read the file line by line
            content = f.readlines()
            for line in content:
                #skip empty lines
                if not line in ['\n', '\r\n']:
                    #delete newline "\n" at the end of the line
                    line = line.replace("\n","")
                    sequences = line.split(";")
                    file.append(sequences)
        return file

    #find the longest common sub-sequence in the lines of the file and print them out
    #Run time complexity: big theta(N)
    #N is the number of items in the "file" list.
    #Since the maximum length of a string in the file is 50, not a big n, I didn't consider it in the run time complexity.
    #If it is considered, the run time complexity will be big theta(I*J*N).
    #I is the number of characters in the left string and J is the number of characters in the right string.

    #Pre-condition: the input parameter of the method is a list containing pairs of strings.
    #Post-condition: the longest common sub-sequence of each pair of strings will be printed out.
    def lcs(this_object):
        fname = input("Please enter the path of a file: ")
        file = this_object.readFile(fname)
        #process sequence pairs line by line
        for sequences in file:
            #left sequence in a line
            seq1 = sequences[0]
            #right sequence in the same line
            seq2 = sequences[1]

            #if the char in seq1 can be found at seq2, store the index of the char in seq2 in a list.
            #one char in seq2 can only be stored once.
            list1 = [None] * len(seq1)
            #False if this index of the character in seq2 has not been stored; True otherwise.
            list2 = [False] * len(seq2)

            #initialize list1
            for i, char1 in enumerate(seq1):
                for j, char2 in enumerate(seq2):
                    if(char1 == char2):
                        if(list1[i] == None and list2[j] == False):
                            list1[i] = j
                            list2[j] = True

            #eliminate the "None" in list1.
            #list1NoNone contains the indexes of chars that both exist in seq1 and seq2. The indexes are the indexes of chars in seq2.
            #The order of the indexes in list1NoNone are the is the same order of the chars in seq1.
            #The problem we need to solve now is to find the longest increasing sequence of indexes.
            list1NoNone = list()
            for i in list1:
                if not i == None:
                    list1NoNone.append(i)

            #all increasing sequences of indexes
            results = list()
            #one increasing sequence of indexes
            resultRound = list()

            #initialize results
            for i in range(len(list1NoNone)):
                for j in range(i + 1, len(list1NoNone)):
                    #the last stored value
                    lastValue = list1NoNone[i]

                   #initiate resultRound
                    resultRound = []
                    resultRound.append(list1NoNone[i])
                    for m in range(j, len(list1NoNone)):
                        if(lastValue < list1NoNone[m]):
                            lastValue = list1NoNone[m]
                            resultRound.append(list1NoNone[m])
                    results.append(resultRound)

            #the indexes of the longest common sub-sequence in seq2
            lcs = None
            #the length of the longest common sub-sequence
            lcsLength = 0
            #find lcs
            for result in results:
                if(len(result) > lcsLength):
                    lcsLength = len(result)
                    lcs = result

            #convert indexes to String
            lcsString = ""
            for i in range(len(lcs)):
                lcsString = lcsString + seq2[lcs[i]]

            #print out the result
            print("The longest common sub-sequence between \"%s\" and \"%s\" is %s" %(seq1, seq2, lcsString))

#start the program by creating an instance of the class and use the instance to call lcs
run = LCS()
run.lcs()