//var str = "HeLLo World! I can't wait to explore your VAST forests. The-End!";
var str = prompt("Enter a string to be translated to Pig Latin: ");

var wordArray = [];
wordArray = str.split(" ");

var output = pigLatin(wordArray);
console.log(output);

function pigLatin(wordArray) {
    var finalString = ""; //translated string
    for (var i = 0; i < wordArray.length; i++) { //for every word in sentence... translate each word
        var cStack = []; //stores indices of capitalized letters
        var exclamationStack = []; //stores indices of exclamation points
        var questionMarkStack = []; //stores indices of question marks
        var periodStack = []; //stores indices of periods
        var apostStack = []; //stores indices of apostrophes
        var word = []; //the single word being analyzed

        word = wordArray[i];

        //format check
        if (word.length == 1) { //checks if it's a single letter
            finalString += word + " ";
            continue;
        }
        if (word.toLowerCase() == "way") { //checks if it is just "way"
            finalString += word + " ";
            continue;
        }

        if (word.search("-") != -1) { //checks if it has a hyphen
            word = hyphen(word); //calls hyphen function which will call pigLatin function
            finalString += word + " ";
            continue;
        }

        for (var j = 0; j < word.length; j++) { //Scan through word for punctuation and capitalization
            //Store indices in stacks and take out punct & caps
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
                periodStack.push(j);
                word = word.replace(".", "");
                var origWord = word;
            }
            if (word[j] == "'") {
                apostStack.push(j);
                word = word.replace("'", "");
                var origWord = word;
            }
            if (word[j] == null) {
                continue;
            }
            if (word[j] == word[j].toUpperCase()) //if capitalized, store index into stack
                cStack.push(j);
        }

        //turn everything into regular text without caps in order to add proper capitalization later
        word = word.toLowerCase();

        //Two ways to translate word into pig latin... depending if it's a vowel or consonant

        //if word starts with a vowel...
        if (word[0] == 'a' || word[0] == 'e' || word[0] == 'i' || word[0] == 'o' || word[0] == 'u') {
            var ending = "way";
            word += ending;
        } else { //if word starts with a consonant
            var ending = word.substr(0, 1) + "ay";
            word = word.substr(1, word.length);
            word += ending;
        }

        var clength = cStack.length; //calls capitalization function to keep proper capitalization
        word = capitalize(word, cStack, clength);

        //adding punctuation back to the word
        for (var y = 0, length = periodStack.length; y < length; y++) {
            var pos = periodStack.pop(); //using stacks to add punctuation back
            var difference = origWord.length - pos; //comparing where the punctuation is relative to end of word
            pos = word.length - difference; //to calculate where it should be in translated word
            word = word.substr(0, pos) + "." + word.substr(pos);
        }
        for (var y = 0, length = exclamationStack.length; y < length; y++) {
            var pos = exclamationStack.pop();
            var difference = origWord.length - pos;
            pos = word.length - difference;
            word = word.substr(0, pos) + "!" + word.substr(pos);
        }
        for (var y = 0, length = questionMarkStack.length; y < length; y++) {
            var pos = questionMarkStack.pop();
            var difference = origWord.length - pos;
            pos = word.length - difference;
            word = word.substr(0, pos) + "?" + word.substr(pos);
        }
        for (var y = 0, length = apostStack.length; y < length; y++) {
            var pos = apostStack.pop();
            var difference = origWord.length - pos;
            pos = word.length - difference;
            word = word.substr(0, pos) + "'" + word.substr(pos);
        }

        finalString += word + " ";
    }
    return finalString;
}


function capitalize(word, stack, length) { //capitalizes the word and returns
    for (var i = 0; i < length; i++) {
        var pos = stack.pop();
        if (pos == 0) { //if first letter is uppercase
            word = word.substr(0, 1).toUpperCase() + word.substr(1);
        }
        if (pos == word.length - 1) { //if last letter is uppercase
            word = word.substr(0, word.length - 1) + word.substr(word.length - 1).toUpperCase();
        }
        if (pos > 0 && pos < word.length - 1) { //if any letters in the middle are uppercased
            word = word.substr(0, pos) + word[pos].toUpperCase() + word.substr(pos + 1);
        }
    }
    return word;
}

function hyphen(word) { //deals with words that have hyphens to be dealt with as two separate words
    var pos = word.search("-");
    var firstWord = word.substr(0, pos); //separating the two words
    var secondWord = word.substr(pos + 1);
    var arr = [];
    arr.push(firstWord);
    arr.push(secondWord);
    var finalWord = pigLatin(arr); //call pigLatin function to translate
    finalWord = finalWord.replace(" ", "-"); //puts words back together
    return finalWord;

}
