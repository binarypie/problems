def main():
    s1=raw_input("Enter first string:")
    s2=raw_input("Enter second string:")

    lngstr=""
    shtstr=""
    newstr=""
    oldstr=""

    if len(s1)<len(s2):
        shtstr=s1
        lngstr=s2
    else:
        shtstr=s2
        lngstr=s1

    for i in range(len(shtstr)):
        ''' PHILOSOPHY
        whenever you find similar strings of character
        just keep checking the next character in the string 
        until you find a difference
        '''
        if shtstr[i] in lngstr[i:]:
            start1=i
            start2=lngstr.index(shtstr[i])
            end1=start1; end2=start2
            
            while (end1<len(shtstr) and end2<len(lngstr)):
                end1+=1; end2+=1
                if shtstr[start1:end1]==lngstr[start2:end2]:
                    newstr=shtstr[start1:end1]
                    if len(newstr)>len(oldstr):
                        oldstr=newstr
                else:
                    break
                
    if len(oldstr)>1:#we dont want one character substrings
        return (oldstr)
    else:
        return ("answer is: 999")    

if __name__ == "__main__":
        print(main())
        