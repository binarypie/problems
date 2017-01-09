# Pig Latin #

> This will take a string, sentance, or paragraph from stdin  and translate it into the pig latin equivilence based on 
the folliwing rules.

* Words that start with a consonant have their first letter moved to the end of the word and the letters “ay” added to the end.
* Words that start with a vowel have the letters “way” added to the end.
* Words that end in “way” are not modified.
* Punctuation must remain in the same relative place from the end of the word.
* Hyphens are treated as two words
* Capitalization must remain in the same place.
* Single letters are not modified.

#Usage

import this into your project, and use the translate function described below:

	"Translate(input *string) string"
This function will take a pointer to a string as input and output the translated pig latin 
string following the above guidelines.

## Example Input ##

    "HeLLo World! I can't wait to explore your VAST forests. The-End!"

## Example Output ##

    "ElLOhay Orldway! I antca'y aitway otay exploreway ouryay ASTVay orestfay. Hetay-Endway!"


#Testing

A short go test suite has been included and can be called with:

	"go test"
