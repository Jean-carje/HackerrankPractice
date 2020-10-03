# Problem
# https://www.hackerrank.com/challenges/electronics-shop/problem
# Score solution: 15.00

# -------------------------------------------
# Soluction 1

def getMoneySpent(keyboards, drives, b):
    temp = 0
    for d in drives:
        for k in keyboards:
            if temp <= (k + d) <= b:
                temp = k + d
    if temp == 0:
        return -1
    return temp


# -------------------------------------------
# Test
# Input

b = 10
keyboards = [3, 1]
drives = [5, 2, 8]

print(getMoneySpent(keyboards, drives, b) == 9)

b = 5
keyboards = [4]
drives = [5]

print(getMoneySpent(keyboards, drives, b) == -1)

