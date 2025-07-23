
from typing import List

"""
73. Set Matrix Zeroes (https://leetcode.com/problems/set-matrix-zeroes/)
Do not return anything, modify matrix in-place instead.

two pass solution
    loop through the entire matrix and for each cell that is zero:
        mark the first element of the row and the first element of the column to zero
    loop through the first row and the first column
        for each row that is marked zero: change entire row to zero
        for each colomn that is marked zero: change entire column to zero
    should be O(n*m) time with O(1) space
    basically using the first row and first column as your memory


note: the first row or first column having zeroes makes your life more difficult especially 
    the top left [0][0] cell in the matrix
    so just skip the first row and first column and have two variables for them insteaad
    (still constant space)

runtime: O(n*m)
space: O(1) - uses the matrix itself to store values thats pretty cool
"""

def setZeroes(matrix: List[List[int]]) -> None:
    n = len(matrix)
    m = len(matrix[0])

    firstrow = any(matrix[0][j] == 0 for j in range(m))
    firstcol = any(matrix[i][0] == 0 for i in range(n))

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for row in range(1, n):
        if matrix[row][0] == 0:
            for j in range(m):
                matrix[row][j] = 0

    for col in range(1, m):
        if matrix[0][col] == 0:
            for i in range(n):
                matrix[i][col] = 0

    if firstrow:
        for j in range(m):
            matrix[0][j] = 0
    if firstcol:
        for i in range(n):
            matrix[i][0] = 0