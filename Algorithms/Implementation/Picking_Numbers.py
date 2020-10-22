# Problem
# https://www.hackerrank.com/challenges/picking-numbers/problem
# Score: 20

#------------------------------------------------
# Solution:
from collections import Counter

def pickingNumbers(a):
    ttl = Counter(a)
    cont = ttl.most_common(2)
    first = max(cont[0][1] + ttl[cont[0][0]+1], cont[0][1] + ttl[cont[0][0]-1])
    second = 0
    if len(cont) > 1:
        second = max(cont[1][1] + ttl[cont[1][0]+1], cont[1][1] + ttl[cont[1][0]-1])
    return max(first, second)

#------------------------------------------------
# Input

ar = [4, 6, 5, 3, 3, 1]
print(pickingNumbers(ar))
ar = [1, 2, 2, 3, 1, 2]
print(pickingNumbers(ar))
ar = [1, 1, 2, 2, 4, 4, 5, 5, 5]
print(pickingNumbers(ar))

ar = '4 2 3 4 4 9 98 98 3 3 3 4 2 98 1 98 98 1 1 4 98 2 98 3 9 9 3 1 4 1 98 9 9 2 9 4 2 2 9 98 4 98 1 3 4 9 1 98 98 4 2 3 98 98 1 99 9 98 98 3 98 98 4 98 2 98 4 2 1 1 9 2 4'.split(' ')
a = [int(n) for n in ar]
print(pickingNumbers(a))

ar = '66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66'.split(' ')
a = [int(n) for n in ar]
print(pickingNumbers(a))
