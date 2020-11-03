# Problem
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# Score: 20

#------------------------------------------------
# Solution 1:
from string import ascii_lowercase

def designerPdfViewer(h, word):
    heights = []
    for w in word:
        i = ascii_lowercase.find(w)
        heights.append(int(h[i]))
    return max(heights) * len(word)
#------------------------------------------------
# Input

h = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5".split(" ")
word = "abc"
print(designerPdfViewer(h, word))
# 9

h = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7".split(" ")
word = "zaba"
print(designerPdfViewer(h, word))
# 28


