def main():
    numPara=int(raw_input("How many paragraphs do you want "))
    numSent=int(raw_input("How many sentences in each paragraph "))

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


    ppess=len(essay)/numPara
    eachpara=[]
    craftpara=""
    
    for i in xrange(len(essay)):
        craftpara+=essay[i]
        if ((i+1)%ppess == 0):
            craftpara=craftpara[0].upper()+str(craftpara[1:])
            eachpara.append(craftpara)
            craftpara=""

    renewedpara=[]
    for i in eachpara:
        lenpara=len(i.split())
        if (lenpara > numSent):
            #each paragraph should have same number of sentences
            renewedpara.append(" ".join(i.split()[0:numSent]))
        else:
            renewedpara.append(i) 

    #finall work
    complessay=[]
    for i in renewedpara:
        j=4
        x=1
        addPer=i.split()
        #place periods after every few words starting from first 4th word
        while j < len(addPer):
            addPer[j]=addPer[j]+str(".") 
            j+=(2*x)+3
            x+=1
        if (addPer[-1][-1]!="."):
            complessay.append(str("\t")+" ".join(addPer)+str(".")+str("\n"))
        else:
            complessay.append(str("\t")+" ".join(addPer)+str("\n"))
        
    print("\n".join(complessay))#print refined essay to console

    #print essay to .txt file
    f = open("generatedEssay.txt","w") 
    f.write("".join(complessay))

if __name__ == "__main__":
        main()