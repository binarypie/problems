def main():
    sentence = raw_input ('Type what you would like translated into pig-latin and press ENTER: ')
    sentence = sentence.split()
    vowels=['a', 'e', 'i', 'o', 'u']
    renewed=[]
    
    lfh=[]
    for i in sentence: #just a little something to deal with hyphens :-)
        if "-" in i:
            j=(i.split("-"))
            lfh.append(j[0]+str("-"))
            lfh.append(str(j[1]))
        else:
            lfh.append(i)        
    sentence=lfh    
 
    for i in sentence:
        if len(i)==1: #for "I"
            renewed.append(i)
            continue
        if (len(i)>=3 and i[-3:]=="way"): #Words that end in "way"
            renewed.append(i)
            continue
        if ((i[0]).lower() not in vowels): #for first letter consonant
            s=(str(i[1:])+str(i[0])+"ay")
            renewed.append(sCapitalize(punctuate(i, s)))
            continue
        if ((i[0]).lower() in vowels): #for first letter vowel
            s=(str(i)+"way")
            renewed.append(sCapitalize(punctuate(i, s)))
            continue
     
    return(" ".join(renewed).replace("- ", "-"))#handling "-"


def sCapitalize((i, s)):#capitalize correctly
    newS=[]
    for k in range(len(i)):
        if (i[k]).isupper():
            newS.append(s[k].upper())
        else:
            newS.append(s[k].lower())
    modstr="".join(newS)
    modstr=modstr+str(s[-(len(s)-len(modstr)):])
    return modstr

def punctuate(i, s):#check for punctuations
    punctuation=[',', '.', '?', '!', '\'', '-' ]
    actualPunc=""
    npi=0
    se=""
    for k in punctuation:
        if k in i:
            npi=i.index(k)
            se=s.replace(k, "")
            actualPunc=k
            break
    npi=npi-len(i)
    if abs(npi)==len(i):
        return (i, s)
    else:
        if len(se[0:npi+len(se)+1]) == len(se):
            return (i, se[0:npi+len(se)+1] + actualPunc)
        else:
            return(i, se[0:npi+len(se)+1] + actualPunc +se[-1])


if __name__ == "__main__":
        x = main()
        print(x)