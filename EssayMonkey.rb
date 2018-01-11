# Essay Monkey #

# > Given a set of txt files generate an essay.
# * The function should take the number of paragraphs to generate.
# * The function should take the number of sentences per peragraph to generate.
# * Each sentence should be of any reasonable length but each should not be the same length.

require 'pry'


def essayMonkey(num_paragraphs, num_sentences)
  parse_file(EssayMonkeyNouns.txt)
  parse_file(EssayMonkeyVerbs.txt)
  parse_file(EssayMonkeyAdjectives.txt)
end

def parse_file(file)
  File.open(file).each do |line|
    return noun_array = line.split(',')
  end
end


puts essayMonkey(1,1)
