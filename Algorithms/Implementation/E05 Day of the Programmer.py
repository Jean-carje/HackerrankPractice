# Problem
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

# Score solution: 15.00

# -------------------------------------------
# Soluction 1 
def dayOfProgrammer(year):
    if 1700 <= year <= 1917:
        if year % 4 == 0 or year % 400 == 0:
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    elif year == 1918:
        return f'26.09.{year}'
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'

# -------------------------------------------
# Test
# Input
year = 2017
print(dayOfProgrammer(year))
year = 2016
print(dayOfProgrammer(year))
year = 1800
print(dayOfProgrammer(year))
year = 1918
print(dayOfProgrammer(year))

# Output
# 13.09.2017
# 12.09.2017
# 12.09.1800