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
  p string_array
end

def change_consonant_starters(word)
  word_array = word.split("")
  first_letter = word_array.shift
  word_array << first_letter
  new_word = word_array.join()
  final_word = new_word + "ay"
  return final_word
end

def change_vowel_starters(word)
end

def is_hyphenated?(word)
end


# p wordify("HeLLo World! I can't wait to explore your VAST forests. The-End!")

p change_consonant_starters("hello")
