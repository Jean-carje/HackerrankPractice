# Problem:
# https://www.hackerrank.com/challenges/magic-square-forming/problem
# score: 20


# --------------------------------------------------------------
# Solution:

def formingMagicSquare(s):
    s = [j for i in s for j in i]
    p = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
    ]

    ttl = []
    for m in p:
        ttl.append(sum([abs(m[i] - s[i]) for i in range(9)]))
        print(ttl)

    return min(ttl)

# --------------------------------------------------------------
# Test
s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
print(formingMagicSquare(s) == 7)
