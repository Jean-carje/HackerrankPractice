# Problem:
# https://www.hackerrank.com/challenges/insertionsort1/problem
# score: 30


# --------------------------------------------------------------
# Solution:

def insertionSort1(n, arr):
    while n > 0:
        j = n - 1
        if j > 0 and arr[j - 1] > arr[j]:
            tp = arr[j]
            arr[j] = arr[j - 1]
            while j > 0 and arr[j - 1] > tp:
                arr[j] = arr[j - 1]
                print(*arr)
                j -= 1
            else:
                arr[j] = tp 
                print(*arr)
        n -= 1

