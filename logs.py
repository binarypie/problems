import re
def CheckLog():
    while True:					
        searchString = input("Enter search string: ")
        matchedLines = ""
        logFile = open("Logs.txt")
        logFileData = logFile.read().split("\n")
        logFile.close()
        for line in logFileData:
            if re.search(searchString,line,re.IGNORECASE):
                matchedLines +=line + "\n"
        print(matchedLines)
        _continue = input("Do you want to coninue?(Y/N): ")
        if(_continue == "N"):
            break

CheckLog()
