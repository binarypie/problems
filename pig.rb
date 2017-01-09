#cap to record place of char that is uppercase
cap = []
#final answer
translation = []

#function to tranlate each word
def change_word(word,cap)
    cap.clear
    find_cap(word,cap)
    word.downcase!
    tmp = " "
    puncs = Hash.new
    for j in 0..word.length
        if word[j] =~ /[^A-Za-z0-9\s]/i
            puncs[word.length-j-3] = word[j]
        end
    end
    word = word.gsub(/[^A-Za-z0-9\s]/i, '')
    if word.length == 1 or word.split(//).last(3).join == "way"
        tmp = word
    elsif word[0] =~ /[aouie]/
        tmp = word + 'way'
        Put_Punc(puncs,tmp)
        
    else
        first = word[0]
        word.slice!(0)
        tmp = word + first + 'ay'
        Put_Punc(puncs,tmp)
        
    end
    Cap(tmp,cap)
    return tmp
end

#function to split string
def pig_latin(w,cap,translation)
    words = w.split
    words.each do |w|
        hyphens = ""
        
        # case of word include hyphens
        if w.include? '-'
            values = w.split('-')
            for i in 0...values.size-1
                
                hyphens += change_word(values[i],cap)+"-"
            end
            hyphens += change_word(values[values.size-1],cap)
            translation << hyphens
            
        else
            translation << change_word(w,cap)
        end
    end
    
    translation.join ' '
end

#find upper case char
def find_cap(word,cap)
    word.each_char do |c|
        if c === c.capitalize
            if c =~ /[^A-Za-z0-9\s]/i or c=~ /[[:digit:]]/
                cap << 0
            else
                cap << 1
            end
        else
            cap << 0
        end
    end
end

#put uppercase char back
def Cap(tmp,cap)
    for i in 0..cap.size
        if cap[i] == 1
            if (tmp[i] =~ /[[:alpha:]]/)
           
                tmp[i] = tmp[i].upcase!
            end
        end
    end
end

#put punctuation back
def Put_Punc(puncs,tmp)
    puncs.reverse_each do |key, value|
        tmp.insert tmp.length-key-2, value
    end
end

#get user input
flag = true
while flag == true
    translation.clear
    puts "Please Enter the string to translate or Q to exit:  "
    str = gets.chomp
    if str == "Q"
        flag = false
    else
        puts pig_latin(str,cap,translation)
    end
end
