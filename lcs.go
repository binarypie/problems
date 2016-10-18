package main

import ("fmt")

func main(){
	var str1,str2 string
	fmt.Print("Enter String 1:")
	fmt.Scan(&str1)
	fmt.Print("Enter String 2:")
	fmt.Scan(&str2)
	lcsString:=lcs(str1,str2)
	if(len(lcsString)==0){
		fmt.Print("There exists no common subsequence.")
	}else{
		fmt.Print("The longest common subsequence is:",lcs(str1,str2))
	}
}

func lcs(str1, str2 string) (string) {
	str1Len := len(str1)
    str2Len := len(str2)
    str1bytes := []byte(str1)
    str2bytes := []byte(str2)
    table := make([][]int, str1Len+1)
    for i := 0; i <= str1Len; i++ {
        table[i] = make([]int, str2Len+1)
    }

    for i := 1; i <= str1Len; i++ {
        for j := 1; j <= str2Len; j++ {
            if str1bytes[i-1] == str2bytes[j-1] {
                table[i][j] = table[i-1][j-1] + 1
            } else if table[i][j-1] > table[i-1][j] {
                table[i][j] = table[i][j-1]
            } else {
                table[i][j] = table[i-1][j]
            }
        }
    }

    lcsString := make([]byte, 0, table[str1Len][str2Len])
    for i, j:= str1Len, str2Len; i > 0 && j> 0; {
        if table[i][j] == table[i-1][j] {
            i--
        } else if table[i][j] == table[i][j-1] {
            j--
        } else {
            lcsString = append(lcsString, str2bytes[j-1])
            i--
            j--
        }
    }

    for i, j := 0, len(lcsString)-1; i < j; i, j = i+1, j-1 {
        lcsString[i], lcsString[j] = lcsString[j], lcsString[i]
    }
	
    return string(lcsString)
}