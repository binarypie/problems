=begin
 Author: Xini Yang
 Date: 01/09/2017
 
 Project: MoneyEssay 
 The function should take the number of paragraphs to generate.
 The function should take the number of sentences per peragraph to generate.
 Each sentence should be of any reasonable length but each should not be the same length.
 
=end
#function to create final essay
def Essay(num_p, num_s)
    textfile = Array['EssayMonkeyNouns.txt','EssayMonkeyVerbs.txt','EssayMonkeyAdjectives.txt']
    list_map  = Hash.new
    for i in 0..2
        x = File.open(File.join(File.dirname(__FILE__), textfile[i]), 'r')
        list_map[i] = x.read.strip.split(',')
        x.close
    end
    essay = ""
    0.upto(num_p-1){
        essay += "  " + Paragraph(list_map,num_s) + "\n\n"
    }
    puts essay
end

#function to create paragraph
def Paragraph(list_map,num)
    para = ""
    sentence_length = (3..[list_map[0].size,list_map[1].size,list_map[2].size].min).to_a.sample num
    paraph = []
    0.upto(num-1){
        paraph << Sentence(list_map,sentence_length.sample)
    }
    para = paraph.join " "
end

#function to create sentence
def Sentence(list_map, num)
    sentence = ""
    j = 0
    0.upto(num-1){
        sentence += list_map[0].sample.strip + " " if j%3 == 0
        sentence += list_map[1].sample.strip + " " if j%3 == 1
        sentence += list_map[2].sample.strip + " " if j%3 == 2
        j += 1
    }
    return sentence.capitalize.strip + "."
end
puts "Enter the Number of Paragraphs: "
paragraphs = gets.chomp.to_i

puts "Enter the Number of Sentences: "
sentence = gets.chomp.to_i
Essay(paragraphs,sentence)
