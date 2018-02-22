# Library imports
import sys

# Constants
PUNCTUATION = ". , ' ; : \" ( ) [ ] } { ! ? + = _ ` ~ | < > / "
DELIMITERS = " \n \t - "
VOWELS = "AaEeIiOoUu"
CONSONANTS = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"

# Returns the first occurence of a delimiter in :string.
def delimiterIndex(string):
	i = 0
	while i < len(string) and string[i] not in DELIMITERS:
		i = i + 1
	return i

# Returns true iff :word ends with character sequence "way".
def endsWithWay(word):
	return len(word) > 2 and word[-3:] == "way"

# Returns :word without any punctuation and capitalization.
def convertToPlain(word):
	plainWord = ""
	word = word.lower()
	for i in range(len(word)):
		if word[i] not in PUNCTUATION:
			plainWord = plainWord+word[i]
	return plainWord

# Turns the characters of :word at the indices in :capIndices into uppercase, returns modified :word.
def addCaps(capIndices, word):
	for i in capIndices:
			word = word[:i] + word[i].upper()+ word[i+1:]
	return word

# Adds to :word punctuation at the indices listed in :puncIndices.
# Each element in :puncIndices is a pair of the puncuation mark and it's index.
def addPunc(puncIndices, word):
	for puncPair in puncIndices:
		i, punc = puncPair
		i = i + len(word) + 1
		word = word[:i] + punc + word[i:]
	return word

# Returns the pig-latin translation of :input_string
def translate(input_string):
	output_string = ""
	while len(input_string) > 0:
		i = delimiterIndex(input_string)
		delimiter = input_string[i] if i < len(input_string) else ""
		word = input_string[:i]
		
		# Indices of all upper case characters in word
		capIndices = [x for x in range(len(word)) if word[x].isupper()]
		# Pairs of all punctuation and their index in word
		puncIndices = [[x-len(word),word[x]] for x in range(len(word)) if word[x] in PUNCTUATION]
		
		word = convertToPlain(word)

		# Translation!
		if len(word) > 1 and not endsWithWay(word):
			if word[0] in CONSONANTS:
				word = word[1:] + word[0] + "ay"
			elif word[0] in VOWELS:
				word = word + "way"

		# Add capitalization and punctuation at the appropriate places in the modified word.
		word = addCaps(capIndices,word)
		word = addPunc(puncIndices, word)
		
		output_string = output_string + word + delimiter
		
		# Update input_string
		input_string = input_string[i+1:]
	return output_string


# Main
infilename, outfilename = sys.argv[1], sys.argv[2]
infile = open(infilename,"r")
outfile = open(outfilename,"w")
for line in infile:
	outfile.write(translate(line))
print("Translation saved in " + outfilename)
infile.close()
outfile.close()
