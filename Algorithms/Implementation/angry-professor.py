# Problem:
# https://www.hackerrank.com/challenges/angry-professor/problem
# score: 20


# --------------------------------------------------------------
# Solution:

def angryProfessor(k, a):
    res = len([i for i in a if i <= 0])
    return 'NO' if res >= k else 'YES'

