var str = "Hello darkness. Can't Wo'man Whodatbe.";
var wordArray = [];
var finalString = "";
wordArray = str.split(" ");
console.log(wordArray);

for (var i = 0; i < wordArray.length; i++) {
    var cStack = [];
    var exclamationStack = [];
    var questionMarkStack = [];
    var periodStack = [];
    var word = [];
    word = wordArray[i];

    if (word.length == 1) {
        finalString += word + " ";
        console.log(finalString);
        continue;
    }
    if (word.toLowerCase() == "way") {
        finalString += word + " ";
    }
    for (var j = 0; j < word.length; j++) {
        console.log("for loop run" + " " + word);
        if (word[j] == word[j].toUpperCase())
            cStack.push(j);
        if (word[j] == "!") {
            exclamationStack.push(j);
            word = word.replace("!", "");
        }
        if (word[j] == "?") {
            questionMarkStack.push(j);
            word = word.replace("?", "");
        }
        if (word[j] == ".") {
            console.log("period check " + word[j])
            periodStack.push(j);
            word = word.replace(".", "");
            console.log("period replace " + word)
            var origWord = word;
        }
        console.log("at end of for loop " + word);
        console.log("period stack" + periodStack);
        console.log("capital stack " + cStack);
    }

    word = word.toLowerCase();

    if (word[0] == 'a' || word[0] == 'e' || word[0] == 'i' || word[0] == 'o' || word[0] == 'u') {
        var ending = "way";
        console.log("word[0] " + word[0])
        word = word.substr(1, word.length);
        console.log("word " + word);
        word += ending;
        console.log(word);
    } else {
        var ending = word.substr(0, 1) + "ay";
        console.log("word[0] " + word[0])
        word = word.substr(1, word.length);
        console.log("word " + word);
        word += ending;
        console.log(word);
    }

    for (var x = 0; x < cStack.length; x++) {
        var count = cStack.pop();
        console.log("cstack pop " + count);
        word[count] = word[count].toUpperCase();
        word = word.substr(0, count) + word[count].toUpperCase() + word.substr(count + 1, word.length);
        console.log(word[count].toUpperCase());
        console.log(word[count]);
        console.log(word);
    }

    for (var y = 0; y < periodStack.length; y++) {
        var pos = periodStack.pop();
        console.log("pos pop " + pos)
        var difference = origWord.length - pos;
        pos = word.length - difference;
        console.log("diff " + difference);
        console.log("pos " + pos)
        word = word.substr(0, pos) + "." + word.substr(pos);
        console.log(word.substr(0, pos));
        console.log(word.substr(pos));
        console.log("word after change: " + word)
    }

    finalString += word + " ";
}

console.log(finalString);
