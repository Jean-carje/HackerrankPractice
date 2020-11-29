# Problem:
# https://www.hackerrank.com/challenges/utopian-tree/problem
# score: 20


# --------------------------------------------------------------
# Solution:

def utopianTree(n):
    h = 1
    if n < 1:
        return h
    for i in range(1, n + 1):
        if i % 2 == 0:
            h += 1
        else:
            h *= 2
    return h

