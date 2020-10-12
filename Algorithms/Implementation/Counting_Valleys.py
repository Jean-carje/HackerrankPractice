# Problem
# https://www.hackerrank.com/challenges/counting-valleys/problem

# Score solution: 15.00

# -------------------------------------------
# Solution 1

def countingValleys(steps, path):
    lvl = 0
    valleys = 0
    for step in path:
        if lvl == 0 and step == 'D':
            valleys += 1

        if step == 'U':
            lvl += 1
        else:
            lvl -= 1
    return valleys

# -------------------------------------------
# Test
# Input

steps = 8
path = 'UDDDUDUU'
print(countingValleys(steps, path))


steps = 12
path = 'DDUUDDUDUUUD'
print(countingValleys(steps, path))

# Output
# 1
# 2
