# Problem
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

# Score: 10

# Solution 
def breakingRecords(scores):
    h_score = scores[0]
    l_score = scores[0]
    high = 0
    low = 0
    for i in scores:
        if i > h_score: 
            h_score = i
            high += 1
        elif i < l_score:
            l_score = i
            low += 1
    return (high, low)


# Input
scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

# Output
# 4 0
