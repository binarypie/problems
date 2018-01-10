def main():
    place=int(raw_input("Enter place"))
    print (0)
    print(1)
    printSequence(place-2, 0, 1)

def printSequence(i, prev, cur):
    if i==0:
        return -1
    else:
        nex=prev+cur
        print (nex)
        prev=cur
        cur=nex
        i-=1
        printSequence(i, prev, cur)


if __name__ == "__main__":
        main()
        