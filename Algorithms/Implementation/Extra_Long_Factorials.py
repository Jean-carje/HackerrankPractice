# Problem
# https://www.hackerrank.com/challenges/extra-long-factorials/problem
# Score: 20

#------------------------------------------------
# Solution 1:
import math

def extraLongFactorials(n):
    print(math.factorial(n))

# Solution 2:
# def extraLongFactorials(n):
    # if n == 1:
        # return 1
    # print(n * extraLongFactorials(n - 1))

#------------------------------------------------
# Input

n = 25
print(extraLongFactorials(n))

n = 45
print(extraLongFactorials(n))

