var str = "Hello darkness my old friend. Can't stop wON't stop! Thien-Tam ditched us all. That is the way!";
var arr = [];
var pigLatinStr = "";
arr = str.split(" ");
console.log(arr);



analyzeEachWord(arr);
console.log(pigLatinStr);

function analyzeEachWord(arr) {
    for (var i = 0; i < arr.length; i++) {
        var word = arr[i];
        console.log(word);
        console.log(pigLatinStr);
        if (arr[i].length > 1) {
            if (word != "way") {
                word = checkCapitalization(arr[i]);
            }
            //var hasHyphen = word.includes("-");
            /*
            if (word.includes("-")) {
              var splitHypenatedWord = word.split("-");
              var firstWord = splitHypenatedWord[0];
              var secondWord = splitHypenatedWord[1];
              firstWord = checkCapitalization(firstWord);
              secondWord = checkCapitalization(secondWord);
              word = firstWord + "-" + secondWord;
            }
            */
        }
        pigLatinStr = pigLatinStr + word + " ";
    }
}

function checkFirstLetter(word) {
    if (word[0] !== 'a' || word[0] !== 'e' || word[0] !== 'i' || word[0] !== 'o' || word[0] !== 'u') {
        word = ifVowel(word[0]);
    } else {
        word = ifConsonant(word[0]);
    }
    return word;
}

function ifConsonant(word) {
    var ending = word.substr(0, 1) + "ay";
    word = word.substr(1, word.length);
    word += ending;
    return word;
}

function ifVowel(word) {
    var ending = "ay";
    word = word.substr(1, word.length);
    word += ending;
    return word;
}

/*
function checkFormat(word) {
  if (word.length == 1) {
    return word;
  }
  if (word == "way")
    return word;
  if (word.includes("-")) {
    var splitHypenatedWord = word.split("-");
    var firstWord = splitHypenatedWord[0];
    var secondWord = splitHypenatedWord[1];
    firstWord = checkCapitalization(firstWord);
    secondWord = checkCapitalization(secondWord);
    word = firstWord + "-" + secondWord;
    return word;
  }
  return word;
}
*/

function checkCapitalization(word) {
    var stack = [];
    for (var i = 0; i < word.length; i++) {
        if (word[i] == word[i].toUpperCase()) {
            stack.push(i);
        }
    }
    word.toLowerCase();
    word = checkFirstLetter(word);

    for (var i = 0; i < stack.length; i++) {
        var count = stack.pop();
        word[count] = word[count].toUpperCase();
    }
    return word;
}
