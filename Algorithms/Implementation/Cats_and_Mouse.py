# Problem
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# Score solution: 15.00

# -------------------------------------------
# Soluction 1

def catAndMouse(x, y, z):
    posA = abs(x - z)
    posB = abs(y - z)
    if posA == posB:
        return 'Mouse C'
    elif posA < posB:
        return 'Cat A'
    else:
        return 'Cat B'


# -------------------------------------------
# Test
# Input

catA = 1
catB = 2
mouse = 3
print(catAndMouse(catA, catB, mouse) == 'Cat B')

catA = 1
catB = 3
mouse = 2
print(catAndMouse(catA, catB, mouse) == 'Mouse C')
