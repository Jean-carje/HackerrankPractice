# Problem
# https://www.hackerrank.com/challenges/the-hurdle-race/problem
# Score: 15

#------------------------------------------------
# Solution:
def hurdleRace(k, height):
    return max(height) - k if max(height) - k > 0 else 0

#------------------------------------------------
# Input

k = 7
height = [2, 5, 4, 5, 2]
print(hurdleRace(k, height))

k = 4
height = [1, 6, 3, 5, 2]
print(hurdleRace(k, height))

# Output
# 0
# 2
