# Essay Monkey #

> Given a set of txt files generate an essay.

* The function should take the number of paragraphs to generate.
* The function should take the number of sentences per peragraph to generate.
* Each sentence should be of any reasonable length but each should not be the same length.

## Input ##

    See EssayMonkeyVerbs.txt
    See EssayMonkeyNouns.txt
    See EssayMonkeyAdjectives.txt

## Testing ##

A simple go test suite is included and can be run with:

	"go test"

more input can be seen by adding the "-v" flag

## Notes ##

Minor alteration was made to EssayMonkeyVerbs.txt. The words were mainly in present/past order
with a couple exceptions. I moved words and added "should've" to match "should"

There is a const in the top of the file which can be changed to have a little more Mass Effect fun
with the generator.

