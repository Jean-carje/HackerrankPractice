# Problem
# https://www.hackerrank.com/challenges/bon-appetit/problem

# Score solution: 15.00

# -------------------------------------------
# Solution 1 
def bonAppetit(bill, k, b):
    del bill[k]
    count = (sum(bill)) // 2
    if count == b: 
        return 'Bon Appetit'
    else: 
        return b - count

# -------------------------------------------
# Test
# Input
bill = [3, 10, 2, 9]
k = 1
b = 12
print(bonAppetit(bill, k, b))
bill = [3, 10, 2, 9]
k = 1
b = 7
print(bonAppetit(bill, k, b))

# Output
# 5
# 'Bon Appetit'
