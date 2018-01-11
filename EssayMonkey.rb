# Essay Monkey #

# > Given a set of txt files generate an essay.
# * The function should take the number of paragraphs to generate.
# * The function should take the number of sentences per peragraph to generate.
# * Each sentence should be of any reasonable length but each should not be the same length.
require 'pry'

def essay_monkey(num_para, num_sen)
  para_generator(num_para, num_sen)
end

def sentence_generator(num_sen)
  nouns = parse_file('EssayMonkeyNouns.txt')
  verbs = parse_file('EssayMonkeyVerbs.txt')
  adj = parse_file('EssayMonkeyAdjectives.txt')
  num_sen.times do |sen|
    noun_idx = rand(0..nouns.length)
    adj_idx = rand(0..adj.length)
    verbs_idx = rand(0..verbs.length)
    random_nouns = nouns[noun_idx]*rand(0..9)
    random_verbs = verbs[verbs_idx]*rand(0..9)
    random_adj = adj[adj_idx]*rand(0..9)
    binding.pry
    puts "#{random_nouns} #{random_verbs} #{random_adj}."
     # "#{verbs[verbs_idx]}"*rand(0..9) "#{adj[adj_idx]}"*rand(0..9)
  end
end

def para_generator(num_para, num_sen)
  num_para.times do |para|
    sentence_generator(num_sen)
  end
end

def parse_file(file)
  File.open(file).each do |line|
    return array = line.split(',')
  end
end

# Generate a sentence.
# Now check the length of all sentences before it within the same paragraph.
  # IF there is a sentence of the same length
      # call the sentence_generator method again
  # ELSE
      # continue onto the next sentence.
  # end
#end

puts essay_monkey(1,1)



#Other alternatives

# Given the num_sen (representing number of sentences), create a hash that is num_sen keys long and assign a random value to each key. This random value will represent the length of the sentence. Double check to make sure all values (sentence lengths) are unique. Then generate the sentences. Do this para_num times.

# {
#   1: 5
#   2: 4
#   3: 6
#   4: 8
#   5: 3
# }
