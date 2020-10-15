# Problem
# https://www.hackerrank.com/challenges/sparse-arrays/problem
# Score: 25.00 points

# ---------------------------------------------------------
# Solution:

def matchingStrings(strings, queries):
    return [strings.count(q) for q in queries]

# ---------------------------------------------------------
# Test:

strings = ["aba", "baba", "aba","xzxb"]
queries = ["aba","xzxb","ab"]

print(matchingStrings(strings, queries))

