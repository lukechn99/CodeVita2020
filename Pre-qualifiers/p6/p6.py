###########################################################
# palindromic count

# given a string with n lowercase characters
# and a list of integers, return the count of
# unique palindromes in that string with the
# lengths of the integers in the list
###########################################################

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
        if length >= len(string):
            continue
        base = 0
        ceiling = length - 1
        while ceiling < len(string):
            if palindrome_helper(string, base, ceiling):
                print("found %s" %(string[base:ceiling]))
                count += 1
            base += 1
            ceiling += 1
    return count

def main():
    # taking input
    length = int(input())
    string = input()
    number_of_palindrome_lengths = input()
    palindrome_lengths = list(map(int, input().split()))
    print(solve(string, palindrome_lengths))

print(solve("abccbaabccba", [1, 3, 5]))