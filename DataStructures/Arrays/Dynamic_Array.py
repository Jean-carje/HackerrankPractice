# Problem
# https://www.hackerrank.com/challenges/dynamic-array/
# Score: 15.00 points

# ---------------------------------------------------------
# Solution:

def dynamicArray(n, queries):
    lastAnswere = 0
    seqList = [[] for _ in range(n)]
    result = []
    for i in queries:
        if i[0] == 1:
            seq = ((i[1] ^ lastAnswere) % n)
            seqList[seq].append(i[2])
        else:
            seq = ((i[1] ^ lastAnswere) % n)
            lastAnswere = seqList[seq][i[2] % len(seqList[seq])]
            result.append(lastAnswere)
    return result

# ---------------------------------------------------------
# Test:

queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
n = 2
print(dynamicArray(n, queries))

# # Output
# 7
# 3
