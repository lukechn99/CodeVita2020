# given one long string and a series of short strings
# determine whether it is possible to recreate the 
# larger string using the short strings.
# The short strings can be connected in any way and
# their characters can be rearranged within the string

# print "YES" if possible and "NO" if not

import sys
import unittest

# use a string hash
def hash(s):
    acc = 0
    for c in s:
        acc += ord(c)
    # this hash allows the length to be stored in the data
    hash = (acc // len(s)) * 100 + len(s)
    return hash
    
# sliding window to look at the substrings of 
# the longer string. Only examine lengths that
# match what we have
def solve(longStr, strList):
    # preliminary check
    if len(longStr) < 1:
        return "NO"
    
    # store short strings in a dictionary
    dict = {}
    for str in strList:
        dict.update({hash(str) : str})
    
    # sliding window
    ptr1 = 0
    ptr2 = 0
    # the window will grow and check
    while ptr2 - ptr1 < len(longStr):
        
    
    
def main():
    longStr = "dogisaloyalanimal"
    strList = ['5', 'a', 'alloy', 'is', 'god', 'lamina']
    print(solve(longStr, strList))
    
class Test(unittest.TestCase):
    def test_stock1(self):
        longStr = "dogisaloyalanimal"
        strList = ['5', 'a', 'alloy', 'is', 'god', 'lamina']
        self.assertEqual(solve(longStr, strList), "YES")
    def test_no1(self):
        longStr = ""
        strList = ["unreached"]
        self.assertEqual

if __name__=="__main__": 
    # main()
    unittest.main()