require_relative 'Parser'

class Sentence

  def initialize
    @verbs = Parser.parse("EssayMonkeyVerbs.txt")
    @adjectives = Parser.parse("EssayMonkeyAdjectives.txt")
    @nouns = Parser.parse("EssayMonkeyNouns.txt")
  end

  # def load_words(args)
  #
  # end

  def generate
    return "#{@nouns.sample } #{@verbs.sample} #{@nouns.sample}."
  end

end
