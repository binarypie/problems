require_relative 'Sentence'
require_relative 'Parser'
require 'pry'

class Essay

  def initialize(num_p, num_s)
    @num_p = num_p
    @num_s = num_s
  end

  def generate
    @essay = []
    @paragraph = []
    @sentence_lengths = []
    @num_p.times do |paragraph|
      @num_s.times do |sentence|
        @sentence = Sentence.new.generate
        @length_of_sentence = @sentence.length
        if (@sentence_lengths).include?(@length_of_sentence)
          @sentence = Sentence.new.generate
        else
          @paragraph << @sentence
          @sentence_lengths << @length_of_sentence
        end
      @essay << @paragraph
      binding.pry
      end
      puts @essay
    end
  end

end

essay = Essay.new(5, 6)
essay.generate




# sentence = Sentence.new
# sentence.load_words({ noun_file: "EssayMonkeyNouns.txt",
#                       verb_file: "EssayMonkeyVerbs.txt",
#                       adj_file: "EssayMonkeyAdjectives.txt"
#                     })
# sentence.generate
# print sentence.generate
