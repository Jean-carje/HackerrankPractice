# Problem
# https://www.hackerrank.com/challenges/sock-merchant/problem

# Score solution: 10.00

# -------------------------------------------
# Soluction 1 
def sockMerchant(n, ar):
    count = 0
    for i in set(ar):
        count += int(ar.count(i) / 2)
    return count
# -------------------------------------------
# Test
# Input
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))

# Output
# 3