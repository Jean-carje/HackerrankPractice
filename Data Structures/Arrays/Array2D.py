# Problem
# https://www.hackerrank.com/challenges/2d-tempray/problem
# Score: 15.00 points

# ---------------------------------------------------------
# Solution:

def hourglassSum(arr):
    contr = 16
    result = []
    row = 0
    while contr > 0:
        for cl in range(4):
            temp = []
            for rw in range(row, row + 3):
                temp.append(arr[cl][rw])
            tp = arr[cl+1][row + 1]
            result.append(sum(temp) + sum(arr[cl + 2][row: row + 3]) + tp)
            contr -= 1
        row += 1

    return max(result)


# ---------------------------------------------------------
# Test:

arr = [[-9, -9, -9, 1, 1, 1],
 [0, -9, 0, 4, 3, 2],
[-9, -9, -9, 1, 2, 3],
 [0, 0, 8, 6, 6, 0],
 [0, 0, 0, -2, 0, 0],
[0, 0, 1, 2, 4, 0]]

print(hourglassSum(arr))
print(hourglassSum(arr) == 28)
