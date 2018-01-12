# PSEUDOCODE

# Example Input
# XMJYAUZ
# MZJAWXU


def cs(string1, string2)
  string1 = string1.split("")
  string2 = string2.split("")
  common_letter = ""
  common_letter(string1, string2)
end

def common_letter(string1, string2)
  string1.each do |char|
    if string2.include(char)
      common_letter = char
    end
  end
  common_letter
end

def store_letters(common_letter, string1, string2)
  a = [string1, string2]

  a.each do |string|
    cl_idx = string.index(common_letter)
    while cl_idx < string.length
      string.to_a
      << string[cl_idx]
  end




# convert the strings to arrays

# refer to the first character in the first string argument.
# => ['X', 'M', 'J', 'Y', 'A', 'U', 'Z']

# if character is present in second string

  # => ['M', 'Z', 'J', 'A', 'W', 'X', 'U']

  # set common_letter = common letter

  # => common_letter = 'X'

# end

  # look at each string beginning from common letter. Store common letter and all following letters into an array.

  # XMJYAUZ
  # array1 = ['X', 'M', 'J', 'Y', 'A', 'U', 'Z']

  # MZJAWXU
    # array2 = ['X', 'U']

    # common_letters = array1 & array2
    # => ['X', 'U']

      # if common_letters.join("").length > longest_common_sub.length

        # longest_common_sub = common_letters.join("")

      # else

        # longest_common_sub = longest_common_sub

      # end

# else (if character is not present in second string)

  # move on to the next character

# end

# return longest_common_sub

# end
