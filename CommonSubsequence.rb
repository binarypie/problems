# PSEUDOCODE


def common_subsequence(string1, string2)
longest_common_sub = ""
final_string = []
string1 = string1.split("")
string2 = string2.split("")






# refer to the first character in the first string argument.

# if character is present in second string

  # look at each string beginning from the common letter. Store the common letter, and all following letters into an array.

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




end
