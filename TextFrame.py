def printframe(maxlength):
    i = 1
    while(i <= maxlength):
        if(i == maxlength):
            print("*")
        else:
            print("*",end='')
        maxlength = maxlength - 1


def printwords(wordslist,maxLength):
	for j in wordslist:
		print('* ' + j.ljust(maxlength) + ' *')

inputframe = input("Enter Text Frame: ")
wordslist = inputframe.split(' ')
maxlength = max(len(word) for word in wordslist)

printframe(maxlength + 4)
printwords(wordslist,maxlength)
printframe(maxlength + 4)
