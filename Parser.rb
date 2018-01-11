require_relative 'Sentence'

module Parser

  def self.parse(file)
    File.open(file).each do |line|
      return array = line.split(',')
    end
  end

end
