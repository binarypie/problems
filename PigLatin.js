var str = "Hello darkness my old friend. Can't stop wON't stop! Thien-Tam ditched us all. That is the way!";
var wordArray = [];
var finalString = "";
wordArray = str.split(" ");

for (var i = 0; i < wordArray.length; i++) {
    var cStack = [];
    var exclamationStack = [];
    var questionMarkStack = [];
    var periodStack = [];
    var word = wordArray[i];
    if (word.length == 1) {
        finalString += word + " ";
        continue;
    }
    if (word.toLowerCase() == "way") {
        finalString += word + " ";
    }
    for (var i = 0; i < word.length; i++) {
        if (word[i] == word[i].toUpperCase())
            cStack.push(i);
        if (word[i] == "!") {
            exclamationStack.push(i);
            word[i].replace("!", "");
        }
        if (word[i] == "?") {
            questionMarkStack.push(i);
            word[i].replace("?", "");
        }
        if (word[i] == ".") {
            periodStack.push(i);
            word[i].replace(".", "");
        }
    }

    word = word.toLowerCase();

    if (word[0] == 'a' || word[0] == 'e' || word[0] == 'i' || word[0] == 'o' || word[0] == 'u') {
        var ending = "way";
        word = word.substr(1, word.length);
        word += ending;
    } else {
        var ending = word.substr(0, 1) + "ay";
        word = word.substr(1, word.length);
        word += ending;
    }

    for (var i = 0; i < cStack.length; i++) {
        var count = cStack.pop();
        word[count] = word[count].toUpperCase();
    }

    for (var i = 0; i < exclamationStack.length; i++) {
        var pos = exclamationStack.pop();
        word = word.substr(0, pos) + "!" + word.substr(pos + 1, word.length - 1);
    }

    for (var i = 0; i < questionMarkStack.length; i++) {
        var pos = questionMarkStack.pop();
        word = word.substr(0, pos) + "?" + word.substr(pos + 1, word.length - 1);
    }

    for (var i = 0; i < periodStack.length; i++) {
        var pos = periodStack.pop();
        word = word.substr(0, pos) + "." + word.substr(pos + 1, word.length - 1);
    }

    finalString += word + " ";
}

console.log(finalString);








/*
Psuedo code:
    function
run through all words in array
if (formatting required)
    return single letter word or word that 's "way"
store capital index in stack
and any punctuation in second stack
lowercase everything
take punctuation out
check
if consonant or vowel
translate word into pig latin
capitalize using stack
add punctuation using stack
append to final string
*/
