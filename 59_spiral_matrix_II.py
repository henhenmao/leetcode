
from typing import List

"""
59. Spiral Matrix II (https://leetcode.com/problems/spiral-matrix-ii/)

create an empty n x n matrix filled with -1s
traverse the matrix in a spiral while filling each cell with 1, 2, 3, .... , n

thats it i'm sure
just copy the same treversing logic from the first spiral matrix problem

runtime: O(n^2)
space: O(n^2)
"""

def generateMatrix(n: int) -> List[List[int]]:

    matrix = [[-1 for _ in range(n)] for _ in range(n)]

    # function below checks if a position is out of bounds or already visited
    # -1 cells are unvisited
    def inBounds(i, j):
        if i < 0 or i >= n or j < 0 or j >= n or matrix[i][j] != -1:
            return False
        return True
        
    # increment to the next direction when an obstacle is encountered
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    i = 0
    j = 0
    k = 0
    num = 1

    # continue moving forward until there is an obstacle in front and to the right
    while True:
        matrix[i][j] = num

        curr = directions[k]
        next_i = i + curr[0]
        next_j = j + curr[1]

        if inBounds(next_i, next_j):
            i = next_i
            j = next_j
            num += 1
            continue
        
        k = (k+1)%4
        curr = directions[k]

        next_i = i + curr[0]
        next_j = j + curr[1]

        if inBounds(next_i, next_j):
            i = next_i
            j = next_j
            num += 1
            continue

        break
    return matrix
    

n = 3
grid = generateMatrix(n)
for row in grid:
    print(row)