
from typing import List

"""
2319. Check if Matrix is X-Matrix (https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/)

simply do a traversal over the matrix
    one diagonal contains all cells of grid[i][j] where i == j
    other diagonal contaisn call cells of grid[i][j] where i == n-j-1

    if you are on a diagonal and grid[i][j] is a 0, return false
    if you are not on a diagonal and grid[i][j] is above 0, return true

runtime: O(n^2)
space: O(1)
"""


def checkXMatrix(grid: List[List[int]]) -> bool:
    n = len(grid)
    
    for i in range(n):
        for j in range(n):
            if i == j or i == n-j-1:
                if not grid[i][j]:
                    return False
            else:
                if grid[i][j]:
                    return False
    return True
