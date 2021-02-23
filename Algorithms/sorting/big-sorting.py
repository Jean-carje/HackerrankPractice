# Problem:
# https://www.hackerrank.com/challenges/big-sorting/problem
# score: 20


# --------------------------------------------------------------
# Solution:

def bigSorting(unsorted):
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted

