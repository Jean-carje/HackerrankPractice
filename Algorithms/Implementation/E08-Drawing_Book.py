# Problem
# https://www.hackerrank.com/challenges/drawing-book/problem

# Score solution: 10.00

# -------------------------------------------
# Soluction 1

def pageCount(n, p):
    if p > n // 2:
        return abs((n+1) - p) // 2 if n % 2 == 0 else abs(n - p) // 2
    elif p > 1:
        return p // 2 if p % 2 != 0 else (p+1) // 2
    return 0


# Soluction 2:

# def pageCount(n, p):
#     count = 0

#     if p > n // 2:
#         if n % 2 == 0 and p == n - 1:
#             return 1
#         for i in range(n, -1, -1):
#             if i == p:
#                 break
#             count += 1
#     else:
#         for i in range(n + 1):
#             if i == p:
#                 break
#             count += 1
#     return count // 2

# -------------------------------------------
# Test
# Input
n = 6
p = 2
print(pageCount(n, p))
n = 5
p = 4
print(pageCount(n, p))
n = 6
p = 5
print(pageCount(n, p))
n = 5
p = 1
print(pageCount(n, p))
n = 7
p = 3
print(pageCount(n, p))

# Output
# 1
# 0
# 1
# 0
# 1