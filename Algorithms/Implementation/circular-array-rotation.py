# Problem:
# https://www.hackerrank.com/challenges/circular-array-rotation/
# score: 20


# --------------------------------------------------------------
# Solution:
from collections import deque

def circularArrayRotation(a, k, queries):
    rot = deque(a)
    rot.rotate(k)
    return list(rot[i] for i in queries)


