__author__ = 'Chenyuan'

#Class ProcessLog contains one method to process a log file.
class ProcessLog(object):

    #Method processLog generates a summary of a log file containing the type and counts for OSs, browsers, IPs, dates, file requested, and referers included in the file.
    #This method also fetches the log records that meet the user's input query.
    #Run time complexity: big theta(N)
    #Pre-condition: fname contains a valid directory to a log file.
    #Post-condition: a summary of a log file containing the type and counts for OSs, browsers, IPs, dates, file requested, and referers included in the file is printed out; and records
    #that meet user's input query are printed out.
    def processLog(this_object, fname):
        #Dictionaries to hold the OS types and their counts. Type is used as the key and count is used as the value.
        OS_dict = dict()
        Browser_dict = dict()
        IP_dict = dict()
        Date_dict = dict()
        file_dict = dict()
        Referer_dict = dict()

        #Read the log file
        with open(fname) as f:
            #read the file line by line
            content = f.readlines()
            for line in content:
                #count the number of records from different IP address and put it in a dictionary
                ipIndex = line.index("- -")
                ip = line[0:(ipIndex - 1)]
                if(ip in IP_dict):
                    IP_dict[ip] = IP_dict[ip] + 1
                else:
                    IP_dict[ip] = 1

                #count the number of records on different date and put it in a dictionary
                date = line[(ipIndex + 5):(ipIndex + 16)]
                if(date in Date_dict):
                    Date_dict[date] = Date_dict[date] + 1
                else:
                    Date_dict[date] = 1

                #count the number of records of different file requested and put it in a dictionary
                fileIndexLeft = line.index("GET")
                fileIndexRight = line.index("HTTP")
                file = line[(fileIndexLeft + 5):(fileIndexRight - 1)]
                if(file in file_dict):
                    file_dict[file] = file_dict[file] + 1
                else:
                    file_dict[file] = 1

                #count the number of records of different referers and put it in a dictionary
                secondQuoteIndex = line.index("\"", fileIndexRight)
                refererIndexLeft = line.index("\"", secondQuoteIndex + 1)
                rerererIndexRight = line.index("\"", refererIndexLeft + 1)
                referer = line[refererIndexLeft + 1:rerererIndexRight]
                if(referer in Referer_dict):
                    Referer_dict[referer] = Referer_dict[referer] + 1
                else:
                    Referer_dict[referer] = 1

                #count the number of records of different browsers and put it in a dictionary
                try:
                    browserIndexLeft = line.index("\"", rerererIndexRight + 1)
                    browserIndexRight = line.index("(")
                    browser = line[browserIndexLeft + 1: browserIndexRight ]
                    if(browser in Browser_dict):
                        Browser_dict[browser] = Browser_dict[browser] + 1
                    else:
                        Browser_dict[browser] = 1
                #special cases when no browser is recorded
                except ValueError:
                    if("no browser" in Browser_dict):
                        Browser_dict["no browser"] = Browser_dict["no browser"] + 1
                    else:
                        Browser_dict["no browser"] = 1

                #count the number of records of different OSs
                #one record in the Logs.txt doesn't have a OS recorded
                #127.0.0.1 - - [19/Jun/2012:09:39:58 +0100] "GET /sGJ.gif HTTP/1.1" 304 0 "-" "Mozilla/4.0 (compatible;)

                #Case 1: the OS information is within a pair of braces
                try:
                    OSIndexRight = line.index(")")
                    OS = line[browserIndexRight + 1: OSIndexRight]
                #Case 2: the OS information is within quotations
                except ValueError:
                    OSIndexLeft = line.index("\"", rerererIndexRight + 1)
                    OSIndexRight = line.index("\"", OSIndexLeft + 1)
                    OS = line[OSIndexLeft + 1: OSIndexRight]

                #Fetch the OS information and put it in a dictionary.
                #If the OS is different from the sample cases here, the whole OS information fetched above will be stored into the dictionary.
                if "Windows NT" in OS:
                    OS = "Windows NT"
                elif "Android" in OS:
                    OS = "Android"
                elif "Mac OS X" in OS:
                    OS = "Mac OS X"
                elif "iOS" in OS:
                    OS = "iOS"

                if(OS in OS_dict):
                    OS_dict[OS] = OS_dict[OS] + 1
                else:
                    OS_dict[OS] = 1

        #Print out the summary of the log file
        print("IP addresses recorded in the", fname,":")
        for key, value in IP_dict.items():
            print("IP: ",key, ",    count: ", value)
        print()
        print("Dates recorded in the", fname,":")
        for key, value in Date_dict.items():
            print("Date: ", key, ", count: ", value)
        print()
        print("File requested in the", fname,":")
        for key, value in file_dict.items():
            print("File: ", key, ", count: ", value)
        print()
        print("Referers recorded in the", fname,":")
        for key, value in Referer_dict.items():
            print("Referer: ", key, ",  count:", value)
        print()
        print("Browsers used in the", fname,":")
        for key, value in Browser_dict.items():
            print("Browser: ", key, ",  count:", value)
        print()
        print("OSs recorded in the", fname,":")
        for key, value in OS_dict.items():
            print("OS: ", key, ",   count:", value)
        print()

        #Accept user queries.
        print("For each of the following entities, enter a specific search query. If you do not wish to specify, just press enter to skip the category.")
        OS = input("OS: ")
        Browser = input("Browser: ")
        IP = input("IP: ")
        Date = input("Date and Time (e.g. 19/Jun/2012:19:16:22): ")
        file = input("File Requested: ")
        Referer = input("Referer: ")

        #Count of the records that meet the user queries
        count = 0
        with open(fname) as f:
            #Read the file line by line
            content = f.readlines()
            for line in content:
                #Print out the records that meet user queries
                if OS in line and Browser in line and IP in line and Date in line and file in line and Referer in line:
                    count = count + 1
                    print(count, ": ", line)
            print("Total number of records: ", count)

#start the program by creating an instance of the class and use the instance to call processLog
run = ProcessLog()
run.processLog("Logs.txt")