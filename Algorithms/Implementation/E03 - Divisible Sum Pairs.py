# Problem
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

# Score: 10

# Soluction 

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in ar[i + 1:]:
            if (ar[i] + j) % k == 0:
                count += 1
    return count


# Input
ar = [1, 3, 2, 6, 1, 2]
n = 6
k = 3
print(divisibleSumPairs(n, k, ar))

# Output
# 5