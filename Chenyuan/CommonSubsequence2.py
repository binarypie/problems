__author__ = 'Chenyuan'

#class Stack is a stack data structure
class Stack():

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    return self.items.append(item)

  def pop(self):
    return self.items.pop()

  def getElements(self):
    return self.items

#version 2.0
#limitation: this algorithm has limitation in dealing with duplicate characters
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
            #create a Stock instance
            #stack is used to hold sub-sequence information
            stack = Stack()
            resultRound.append(list1NoNone[0])
            #string version of resultRound
            resultRoundString = str(list1NoNone[0])
            #sub-sequence information used to put into the stack.
            #-1 represents a value that is always smaller than any other value, which are all indexes and larger than or equal to 0.
            info = "-1" + "\n" + str(0)
            #push the information into the stack
            stack.push(info)
            #the value of the last item
            lastValue = list1NoNone[0]

            #search for the first sub-sequence and initialize the stack
            for i in range(1, len(list1NoNone)):
                if(lastValue < list1NoNone[i]):
                    lastValue = list1NoNone[i]
                    resultRound.append(list1NoNone[i])
                    info = resultRoundString + "\n" + str(i)
                    resultRoundString = resultRoundString + ";" + str(list1NoNone[i])
                    stack.push(info)
            results.append(resultRound)


            #pop out the items from the stock to search for other possible sub-sequences
            while(not stack.isEmpty()):
                resultRound = list()
                info = stack.pop()
                infos = info.split()
                values = infos[0].split(";")
                lastValue = int(values[len(values) - 1])
                if not values[0]=="-1":
                    resultRoundString = values[0]
                    resultRound.append(int(values[0]))
                else:
                    resultRoundString = ""
                info2 = None
                for m in range(1, len(values)):
                    if resultRoundString == "":
                        resultRoundString = values[m]
                    else:
                        resultRoundString = resultRoundString + ";" + values[m]
                    resultRound.append(int(values[m]))
                if (int(infos[1]) + 1) < len(list1NoNone):
                    for j in range(int(infos[1]) + 1, len(list1NoNone)):
                        if lastValue < list1NoNone[j]:
                            lastValue = list1NoNone[j]
                            resultRound.append(list1NoNone[j])
                            if resultRoundString == "":
                                resultRoundString = "-1"
                            info2 = resultRoundString + "\n" + str(j)
                            resultRoundString = resultRoundString + ";" + str(list1NoNone[j])
                            stack.push(info2)
                if not info2 == None:
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
