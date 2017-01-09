=begin 
PigLatin Project
 - Words that start with a consonant have their first letter moved to the end of the word and the letters “ay” added to the end.
 - Words that start with a vowel have the letters “way” added to the end.
 - Words that end in “way” are not modified.
 - Punctuation must remain in the same relative place from the end of the word.
 - Hyphens are treated as two words
 - Capitalization must remain in the same place.
 - Single letters are not modified.
 
 Author: Xini Yang
 Date: 01/09/2017
=end

#function to split string
def pig_latin(w)
    translation = []
    words = w.split
    words.each do |w|
        hyphens = ""
        
        # case of word include hyphens
        if w.include? '-'
            values = w.split('-')
            for i in 0...values.size-1
                hyphens += change_word(values[i])+"-"
            end
            hyphens += change_word(values[values.size-1])
            translation << hyphens
        else
            translation << change_word(w)
        end
    end
    
    translation.join ' '
end

#function to tranlate each word
def change_word(word)
    cap = []
    find_cap(word,cap)
    word.downcase!
    tmp = " "
    puncs = Hash.new
    for j in 0..word.length
        puncs[word.length-j-1] = word[j] if word[j] =~ /[^A-Za-z0-9\s]/i
    end
    word = word.gsub(/[^A-Za-z0-9\s]/i, '')
    if word.length == 1 or word.split(//).last(3).join == "way"
        tmp = word
    elsif word[0] =~ /[aouie]/
        tmp = word + 'way'
    else
        first = word[0]
        word.slice!(0)
        tmp = word + first + 'ay'
    end
    Put_Punc(puncs,tmp)
    Cap(tmp,cap)
    return tmp
end



#find upper case char
def find_cap(word,cap)
    word.each_char do |c|
        c =~ /[ABCDEFGHIJKLMNOPQRSTUVWXYZ]/ ? (cap << 1) : (cap << 0)
    end
end

#put uppercase char back
def Cap(tmp,cap)
    for i in 0..cap.size
          tmp[i] = tmp[i].upcase! if cap[i] == 1 && (tmp[i] =~ /[[:alpha:]]/)
    end
end

#put punctuation back
def Put_Punc(puncs,tmp)
    puncs.reverse_each do |key, value|
        tmp.insert tmp.length- key, value
    end
end

#get user input
flag = true
while flag == true
    puts "Please Enter the string to translate or Q to exit:  "
    str = gets.chomp
    str == "Q" ? (flag = false) : (puts pig_latin(str))
end


