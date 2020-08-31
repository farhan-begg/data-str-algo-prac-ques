# given a string find first non repeating character and return index
# if no index return -1


#[ "a", "b", "c", "c", "e"]


s = ["bs", "aa", ]

# function get_repeat (array_1)

# hashtable

# loop through array a
# if there is no letter add it to hashtable
# if there is add value +1

#  there is same letter return -1


def fist_unique_character(s):
    hash_table = {}

    for char in s:
        if char in hash_table:
            hash_table[char] = hash_table[char] + 1
        else:
            hash_table[char] = 1

    for i, char in enumerate(s):
        if hash_table[char] == 1:

            return i

    return -1


print(fist_unique_character(s))
fist_unique_character(s)
