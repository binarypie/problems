require 'pry'
# def pig_latinify(string)
#   sentence_array = string.split(" ")
#   if string[0].include(vowels)?
#     change_vowel_starters
#   else
#     change_consonant_starters
#   end
# end



# Helper Methods

def wordify(string)
  # string_array = string.split( /\s+|\b/ )
  string_array = string.split( /\s+|\!|\-|\.|\,/ )
end

def change_consonant_starters(word)
  word_array = word.downcase.split("")
  first_letter = word_array.shift
  # if word_array.include(a special character)
  word_array << first_letter
  new_word = word_array.join()
  final_word = new_word + "ay"
  if word[0] && word[0].capitalize === word[0]
    return final_word.capitalize!
  else
    return final_word
  end
end

def change_vowel_starters(word)
  word_array = word.split("")
end

def is_hyphenated?(word)
end


wordified = wordify("HeLLo World! I can't wait to explore your VAST forests. The-End!")

vowel = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
punctuation = ['!', '.', '?']

wordified.each do |word|
  # binding.pry
  if vowel.include?(word[0])
    puts "Vowerl word: #{word}"
  elsif word == ""
    puts "special char"
  else
    puts change_consonant_starters(word)
  end
end

# p change_consonant_starters(wordified)
