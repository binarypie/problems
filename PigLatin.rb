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

def wordify(sentence)
  return sentence_array = sentence.split(" ")
  # return sentence_array = sentence.split( /\s+|\b/ )
  # return sentence_array = sentence.split( /\s+|\!|\-|\.|\,/ )
  # p sentence_array = sentence.split( /\s+|\b|\W/ )
end

def change_consonant_starters(word)
  word_array = word.downcase.split("")
  first_letter = word_array.shift
  # binding.pry
  if /\W/.match(word_array[-1]).class == MatchData
    final_word = word_array.insert(-2, first_letter+"ay").join
  else
    word_array << first_letter
    final_word = word_array.join + "ay"
  end
  if word[0] && word[0].capitalize === word[0]
    return final_word.capitalize!
  else
    return final_word
  end
end

def change_vowel_starters(word)
  word_array = word.split("")
  if /\W/.match(word_array[-1]).class == MatchData
    final_word = word_array.insert(-2, "way").join
  else
    final_word = word + "way"
  end
end

def is_hyphenated?(word)
end

def end_with_way?(word)
  word[-3..-1] == "way"
end


# p wordified = wordify("HeLLo World! I can't wait to explore your VAST forests. The-End!")
# p wordified.join("")

puts change_consonant_starters("Hello!")
puts change_vowel_starters("Apple!")


# def pig_latinify(sentence)
#   vowel = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#   wordify(sentence).each do |word|
#     if vowel.include?(word[0])
#       change_vowel_starters(word)
#     else
#       change_consonant_starters(word)

# wordified.each do |word|
#   # binding.pry
#   if vowel.include?(word[0])
#     puts "Vowel word: #{word}"
#   elsif word == /\W/
#     puts word
#   else
#     puts change_consonant_starters(word)
#   end
# end

# p change_consonant_starters(wordified)
