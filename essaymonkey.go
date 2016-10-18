package main

import ("fmt"
		"math/rand"
		"bytes"
		"io/ioutil"
		"strings"
		)

func main(){
	var n_para,n_sent int
	fmt.Print("Enter number of paragraphs:")
	fmt.Scan(&n_para)
	fmt.Print("Enter number of sentences per paragraph:")
	fmt.Scan(&n_sent)
	for para:=0;para<n_para;para++{
		fmt.Print("\n\n\t")
		for sentence:=0;sentence<n_sent;sentence++{
			fmt.Print(generateSentence())
		}
	}
}

func randomSentenceStructure() string{
	sentenceStruct:= [6]string{"anv,anv","anv","nvan","nva,van","anv,nvan","anv,nnv"}
	return (sentenceStruct[rand.Intn(5)])
}

func generateSentence()string{
	var word string
	var err error
	var sentence bytes.Buffer
	verbFile,err:= ioutil.ReadFile("EssayMonkeyVerbs.txt")
	check(err)
	verbs := strings.SplitN(string(verbFile),",",-1)
	nounFile,err:= ioutil.ReadFile("EssayMonkeyNouns.txt")
	check(err)
	nouns := strings.SplitN(string(nounFile),",",-1)
	adjFile,err:= ioutil.ReadFile("EssayMonkeyAdjectives.txt")
	check(err)
	adj := strings.SplitN(string(adjFile),",",-1)
	structure:= randomSentenceStructure()
	
	for i:=0;i<len(structure);i++{
		if(structure[i]!=','){
			if structure[i]=='a'{
				word=adj[rand.Intn(len(adj)-1)]
			}	
			if structure[i]=='n'{
				word=nouns[rand.Intn(len(nouns)-1)]
			}	
			if structure[i]=='v'{
				word=verbs[rand.Intn(len(verbs)-1)]
			}
		}else{
			word="and"
		}
	sentence.WriteString(" "+word)
	}
	return sentence.String()+"."
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}