###########################################################
# palindromic count

# given a string with n lowercase characters
# and a list of integers, return the count of
# unique palindromes in that string with the
# lengths of the integers in the list
###########################################################

import unittest

# takes a string, and the indices to check between
def palindrome_helper(string, base, ceiling):
    if ceiling - base <= 1:
        return True
    elif string[base] == string[ceiling]:
        return palindrome_helper(string, base + 1, ceiling - 1)
    else:
        return False
    
# uses sliding window of each length to look for palindromes
# this is a brute force solution
def solve(string, palindrome_lengths):
    count = 0
    for length in palindrome_lengths:
        # skip if palin query is longer than string
        if length > len(string):
            continue
        base = 0
        ceiling = length - 1
        while ceiling < len(string):
            if palindrome_helper(string, base, ceiling):
                count += 1
            base += 1
            ceiling += 1
    return count

# solve in one pass
def solve1(string, palindrome_lengths):
    pass

def main():
    # taking input
    length = int(input())
    string = input()
    number_of_palindrome_lengths = input()
    palindrome_lengths = list(map(int, input().split()))
    print(solve(string, palindrome_lengths))

class Test(unittest.TestCase):
    def test_tcs1(self):
        string = "xyxzyxyz"
        lengths = [1, 3, 5]
        self.assertEqual(solve(string, lengths), 11)
    def test_tcs2(self):
        string = "abccbaabccba"
        lengths = [4, 6, 12]
        self.assertEqual(solve(string, lengths), 7)

if __name__=="__main__": 
    main()
    # unittest.main()