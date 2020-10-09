# Problem
# https://www.hackerrank.com/challenges/the-birthday-bar/problem

# Score: 10

# Solution 

def birthday(s, d, m):
    count = 0
    for i in range((len(s)-m) + 1 ):
        if sum(s[i:i+m]) == d:
            count += 1
    return count


# Input
s = [1, 2, 1, 3, 2]
d = 3
m = 2
print(birthday(s, d, m))

# Output
# 2
