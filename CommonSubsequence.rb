# PSEUDOCODE

# Example Input
# XMJYAUZ
# MZJAWXU

# convert the strings to arrays

# refer to the first character in the first string argument.
# => ['X', 'M', 'J', 'Y', 'A', 'U', 'Z']

# if character is present in second string

  # => ['M', 'Z', 'J', 'A', 'W', 'X', 'U']

  # set common_letter = common letter

  # => common_letter = 'X'

# end

  # look at each string beginning from common letter. Store the common letter, and all following letters into an array.

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
