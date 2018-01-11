require 'pry'


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

  # def is_hyphenated?(word)
  #   if word.include("-")
  # end

  def ends_with_punctuation?
    /\W/.match(word_array[-1]).class == MatchData
  end

  def has_apostrophe?
    if word.include("'")
  end

  def end_with_way?(word)
    word[-3..-1] == "way"
  end



sentence = "HeLLo World! I can't wait to explore your VAST forests. The-End!"
vowel = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
final_sentence = []
wordify("HeLLo World! I can't wait to explore your VAST forests. The-End!").each do |word|
  if vowel.include?(word[0])
    final_sentence << change_vowel_starters(word)
  else
    final_sentence << change_consonant_starters(word)
  end
end
puts final_sentence
end




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


# p wordified = wordify("HeLLo World! I can't wait to explore your VAST forests. The-End!")
# # p wordified.join("")
#
puts change_consonant_starters("Hello!")
puts change_vowel_starters("Apple!")
puts change_consonant_starters("Can't")
# puts wordify("HeLLo World! I can't wait to explore your VAST forests. The-End!")
