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
    puts "#{nouns[noun_idx]} #{verbs[verbs_idx]} #{adj[adj_idx]}."
  end
end

def para_generator(num_para, num_sen)
  num_para.times do |para|
    sentence_generator(num_sen)
  end
end

def parse_file(file)
  File.open(file).each do |line|
    return noun_array = line.split(',')
  end
end


puts essay_monkey(1,5)
