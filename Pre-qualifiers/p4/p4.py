###########################################################
# T9 Inverse

# - Problem Description
# Suppose you have a mobile phone which has a large set of
# contacts. At times it might get tedious to search a group
# of contacts, for e.g. names that contain certain
# alphabets in the name, not necessarily begins with that
# alphabet. As you know, in a common dial-pad each digit
# from 2 to 9 is associated with some alphabets. When a
# number key is pressed all the names in the contact list 
# which have any characters corresponding to the pressed 
# numerical key are shown in the search result. For e.g. 
# If numerical key 7 is pressed, all the names in contact
# list that have characters ( p s) anywhere in the contact
# names are shown. If a second key is pressed, all
# combinations of first key characters an second key
# characters that appear in the contact names in the same
# order are shown in the search result. For example, if 7
# is the first key that is pressed and 4 is the second key
# that is pressed, then all contact names that can be
# formed out of combination operation of (p. q, r s) and
# (g, h, i), in an order preserving manner ie. 7-key
# characters followed by 4-key characters viz
# (pg, ph. pi, qg, gh, gi, rg, rh, ri, sg, sh, si) are
# shown in the search result. Similarly, if a third key is
# pressed, there will be even more number of combinations
# that will be searched by the phone. Write a code to find
# which numerical keys should be pressed in what order if
# the desired search result is provided as input. If there
# are two or more key combinations to get the desired
# contact list, print the lexographically greater value as
# output

# - Constraints
# 1 < S < 1000

# - Input
# First line contains a string S denoting all the contact
# names separated by space that need to be obtained as a
# outcome of search operation

# - Output
# Print lexicographically greater value as number key
# patterns which when pressed in that order would produce
# the input string S. Print "NA", if no key combinations
# are possible to get all the names in one search
# operations

# - Time Limit
# 1

# - Examples
# Example 1:
# Input:
# Abhishek Ipsita Kamlesh Nisha Yash Sharon

# Output:
# 74

# Explanation
# Assume that the contact list contains only first names
# Abhishek, Kamlesh, Nisha, Yash and Sharon, all contain
# Ipsita contains si. Hence pressing key 7 followed by key
# 4 will give the expected search result
###########################################################

keypad = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"]
}

def solve(names):
    pass