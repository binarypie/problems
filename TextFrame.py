def main():
    sentence=raw_input("Enter sentence you want to frame: ")
    liswrds=sentence.split()
    lenlis=[]
    result=""

    for i in liswrds:
        lenlis.append(len(i))
    length=max(lenlis)
    
    #top of frame
    top = str("**")+str((length+1)*"*")+str("*\n")
    result+=top

    for i in liswrds:
        result+=str("* ")+str(i)+str(((len(top)-1)-
        len(i)-3)*" ")+str("*\n")

    #bottom of frame
    result+=top   

    return result


if __name__ == "__main__":
        print(main())