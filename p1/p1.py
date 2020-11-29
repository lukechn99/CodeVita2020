# given two natural numbers, find the number of steps to get from one to another
# can be represented as a graph

import sys

# creates a list of numbers followed by their biggest factor
def factorList(n):
    factors = [n]
    while factors[-1] != 1:
        for i in reversed(range(factors[-1])):
            if factors[-1] % i == 0:
                factors.append(i)
                break
    return factors

def solve(n, m):
    factorsN = factorList(int(n))
    factorsM = factorList(int(m))
    print(factorsN)
    print(factorsM)
    for i in range(len(factorsN)):
        for j in range(len(factorsM)):
            if factorsN[i] == factorsM[j]:
                return i + j
    return -1

def main():
    if len(sys.argv) < 3:
        print("Provide 2 natural numbers")
        sys.exit(1)
    print(solve(sys.argv[1], sys.argv[2]))
    
if __name__=="__main__": 
    main()