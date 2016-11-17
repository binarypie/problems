//var str = "Hello darkness. Can't Wo'man Whodatbe.";
var str = "HeLLo DarKnesS";
var wordArray = [];
var finalString = "";
wordArray = str.split(" ");
console.log(wordArray);

for (var i = 0; i < wordArray.length; i++) {
    var cStack = [];
    var exclamationStack = [];
    var questionMarkStack = [];
    var periodStack = [];
    var apostStack = [];
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
    for (var j = 0; j < word.length; j++) { //Wo'man   Oman'way
        console.log("for loop run" + " " + word);
        if (word[j] == null) {
          continue;
        }
        if (word[j] == word[j].toUpperCase()) //cstack pushed 0
            cStack.push(j);
        if (word[j] == "!") {
            exclamationStack.push(j);
            word = word.replace("!", "");
            var origWord = word;
        }
        if (word[j] == "?") {
            questionMarkStack.push(j);
            word = word.replace("?", "");
            var origWord = word;
        }
        if (word[j] == ".") {
            console.log("period check " + word[j])
            periodStack.push(j);
            word = word.replace(".", "");
            console.log("period replace " + word)
            var origWord = word;
        }
        if (word[j] == "'") { //apoststack pushed 2
            apostStack.push(j);
            word = word.replace("'", ""); //Woman
            var origWord = word;
        }
        console.log("at end of for loop " + word);
        console.log("period stack" + periodStack);
        console.log("capital stack " + cStack);
    }

    word = word.toLowerCase(); //woman

    if (word[0] == 'a' || word[0] == 'e' || word[0] == 'i' || word[0] == 'o' || word[0] == 'u') {
        var ending = "way";
        console.log("word[0] " + word[0])
        word = word.substr(1, word.length);
        console.log("word " + word);
        word += ending;
        console.log(word);
    } else {
        var ending = word.substr(0, 1) + "ay"; //way
        console.log("word[0] " + word[0])
        word = word.substr(1, word.length); //oman
        console.log("word " + word);
        word += ending; //omanway
        console.log(word);
    }
    var clength = cStack.length;
    word = capitalize(word, cStack, clength);

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



function capitalize(word, stack, length) { //omanway stack with 0 and 3
  for (var i = 0; i < length; i++) {
    var pos = stack.pop();
    if (pos == 0) {
      word = word.substr(0, 1).toUpperCase() + word.substr(1);
    }
    if (pos == word.length - 1) {
      word = word.substr(0, word.length - 1) + word.substr(word.length - 1).toUpperCase();
    }
    if (pos > 0 && pos < word.length-1) {
		word = word.substr(0, pos) + word[pos].toUpperCase() + word.substr(pos+1);
    }
  }
  return word;
}
