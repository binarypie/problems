import random

def main():
    numPara=int(raw_input("How many paragraphs do you want: "))
    numSent=int(raw_input("How many sentences in each paragraph: "))

    #open files and read
    fverbs = open("EssayMonkeyVerbs.txt","r") 
    fadj = open("EssayMonkeyAdjectives.txt","r") 
    fnoun = open("EssayMonkeyNouns.txt","r") 

    strverbs=fverbs.read()
    stradj=fadj.read()
    strnoun=fnoun.read()

    #replace commas with spaces
    essay=str(strverbs)+str(stradj)+str(strnoun)
    essay=essay.replace(",", " ").replace("\t", " ").replace("\n", " ").replace("  ", " ")

    newessay="\t" #indent first word from first paragraph
    for i in range(numPara):
        j=0
        esslis=essay.split(" ")
        prepo=random.randint(0, 5)
        nexpo=random.randint(5, 10)
        #randomly select few number of 
        #words after which we add a period
        nesspara=""
        while (j < numSent) and (nexpo < len(esslis)):
            nesspara+=" ".join(esslis[prepo:nexpo])+str(". ")
            temp=prepo
            prepo=nexpo
            nexpo+=(random.randint(temp, temp+random.randint(15, 20))) #randomly pick where to add periods
            j+=1
        newessay+=nesspara+str("\n\t")
    return(newessay)

if __name__ == "__main__":
        print(main())
