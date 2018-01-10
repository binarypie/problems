def main():
    sentence = raw_input ('Type what you would like translated into pig-latin and press ENTER: ')
    sentence = sentence.split()
    vowels=['a', 'e', 'i', 'o', 'u']
    renewed=[]
    for i in sentence:
        if len(i)==1:
            renewed.append(i)
            continue
        if (len(i)>=3 and i[-3:]=="way"):
            renewed.append(i)
            continue
        if ((i[0] not in vowels)):
            s=(str(i[1:])+str(i[0])+"ay")
            renewed.append(punctuate(i,s))
            continue
        if i[0] in vowels:
            s=(str(i)+"way")
            renewed.append(punctuate(i,s))
            continue
    return(" ".join(renewed))

def punctuate(i, s):
    punctuation=[',', '.', '?', '!', '\'', ]
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
        return s
    else:
        if len(se[0:npi+len(se)+1]) == len(se):
            return (se[0:npi+len(se)+1] + actualPunc)
        else:
            return(se[0:npi+len(se)+1] + actualPunc +se[-1])


if __name__ == "__main__":
        x = main()
        print(x)