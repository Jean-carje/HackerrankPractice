# Problem
# https://www.hackerrank.com/challenges/migratory-birds/problem

# Score solution 1: 7.50
# Score solution 2: 10

# -------------------------------------------
# Soluction 1 
# from collections import Counter
# def migratoryBirds(arr):
#     return Counter(arr).most_common()[0][0]

# Soluction 2   
def migratoryBirds(arr):
    birds = [0]*6
    for i in arr:
        birds[i] += 1
    return birds.index(max(birds))

# -------------------------------------------
# Test
# Input
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
# arr = [1, 4, 4, 4, 5, 3]
print(migratoryBirds(arr))

# Output
# 3
# Output
# 4