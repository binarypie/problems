# SENTENCE SPLITTER

  def wordify(sentence)
    return sentence_array = sentence.split(" ")
  end

# WORD DETERMINER (#Will the word be transformed? And if so, how?)

  def determine_and_translate(word)
    vowels = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if word.length == 0 || word.length == 1
      return word
    elsif ends_with_way?(word)
      return word
    elsif vowels.include? word[0]
      return change_vowel_starters(word)
    else
      return change_consonant_starters(word)
    end
    return word
  end

# ACTIONS TO FOLLOW DEPENDING ON TYPE OF WORD

  def change_consonant_starters(word)
    word_array = word.downcase.split("")
    first_letter = word_array.shift
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

# HELPER METHODS

  def has_punctuation?
    true if word.include(/[[:punct:]]/)
    # /\W/.match(word_array[-1]).class == MatchData
  end

  def has_apostrophe?
    true if word.include("'")
  end

  def ends_with_way?(word)
    word[-3..-1] == "way"
  end

# FINAL METHOD

def pig_latin(sentence)
  words = wordify(sentence)
  final_sentence = []
  words.each do |word|
    if word.include? '-'
      first,second=word.split("-")
      latinified = "#{determine_and_translate(first)}-#{determine_and_translate(second)}"
    else
      latinified = determine_and_translate(word)
    end
  final_sentence << latinified
  end
  return final_sentence.join(" ")
end

# USER INTERFACE

puts "Welcome to the Pig Latin Translator! Please enter a word or sentence you would like to translate. Type '1' to exit:"
input = gets.chomp
until input == "1"
    puts pig_latin(input)
    puts "Enter another word or sentence to tranlate or type '1' to exit: "
    input = gets.chomp
end




# TEST CASES BELOW


# sentence = "HeLLo World! I can't wait to explore your VAST forests. The-End!"
# puts determine_and_translate("Hello!")
# puts change_consonant_starters("Hello!")
# puts change_vowel_starters("Apple!")
# puts change_consonant_starters("Can't")
# puts pig_latin(sentence)
# puts pig_latin("Callaway")
