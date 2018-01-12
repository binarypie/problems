require_relative 'Sentence'
require_relative 'Parser'

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
          @paragraph << @sentence.capitalize
          @sentence_lengths << @length_of_sentence
        end
      end
      @essay << @paragraph
    end
    @essay.each do |paragraph|
      puts paragraph.join(" ")
    end
  end

end

######### RUNNER (CMD LINE) ############

puts "Welcome to the essay generator! How many paragraphs would you like your essay to have? Please enter an integer (i.e. 4)."
input_1 = gets.chomp

if input_1.to_i == 0
  until !(input_1.to_i == 0)
    puts "Ooh... looks like you didn't enter an integer or you entered 0! Let's try that again. Please enter an integer greater than 0 (i.e. 4)."
    input_1 = gets.chomp
  end
  num_p = input_1.to_i
else
  num_p = input_1.to_i
end

puts "Great! Your essay will contain #{num_p} paragraphs. How many sentences would you like each paragraph to have? Please enter an integer (i.e. 5)."
input_2 = gets.chomp

if input_2.to_i == 0
  until !(input_2.to_i == 0)
    puts "Ooh... looks like you didn't enter an integer or entered 0! Let's try that again! Please enter an integer greater than 0 (i.e. 4)."
    input_2 = gets.chomp.to_i
  end
  num_s = input_2.to_i
else
  num_s = input_2.to_i
end

puts essay = Essay.new(num_p, num_s).generate
