# Problem
# https://www.hackerrank.com/challenges/array-left-rotation/problem
# Score: 20.00 points

# ---------------------------------------------------------
# Solution:

def rotateLeft(d, arr):
    return arr[d:] + arr[:d]


# ---------------------------------------------------------
# Test:

d = 4
ar = [1,2,3,4,5]

print(rotateLeft(d, ar))

