

from typing import List

"""
221. Maximal Square (https://leetcode.com/problems/maximal-square/description/)

plan: to recursively build squares by building off of previous squares
start from the bottom right of the matrix and increment backwards

i will define a cell "containing" a square by the cell being the top left
    corner of any square
i will define the "size" of the square by the length and width (nxn)

for any given cell at matrix[i][j]:
    if matrix[i][j-1] and matrix[i-1][j] both contain a square of at least n 
        (just take the min of each):
        let S be the min size that matrix[i][j-1] and matrix[i-1][j] contain
        check matrix[i-S][j-S] since the bottom right corner is the only thing
        left to check
    if all conditions are met then you can conclude that matrix[i][j]
    contains a square of size S+1

runtime: O(n * m) where n is the length and m is the width of the matrix
space: O(n * m) since we are storing items in dp


"""

def maximalSquare(matrix: List[List[str]]) -> int:
    n = len(matrix)
    m = len(matrix[0])

    def inBounds(x, y):
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        return True

    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            curr = matrix[i][j]
            if curr == "0":
                continue

            dp[i][j] = 1

            if not (inBounds(i+1, j) and inBounds(i, j+1)):
                continue

            right = dp[i][j+1]
            bottom = dp[i+1][j]

            if right == 0 or bottom == 0:
                continue

            size = min(right, bottom)

            for s in range(size, 0, -1):
                if matrix[i+s][j+s] == "1":
                    dp[i][j] = s+1
                    break

    return (max(map(max, dp))**2)