
from typing import List
from collections import defaultdict

"""
3446. Sort Matrix by Diagonals (https://leetcode.com/problems/sort-matrix-by-diagonals/description/?envType=daily-question&envId=2025-08-28)



"""



def sortMatrix(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    diagonals = defaultdict(list)

    for row in range(n):
        for col in range(n):
            diagonals[row-col].append(grid[row][col])
    
    for k in diagonals:
        if k >= 0: # bottom left
            diagonals[k].sort()
        else:
            diagonals[k].sort(reverse=True)

    for row in range(n):
        for col in range(n):
            grid[row][col] = diagonals[row-col].pop()

    return grid
    


grid = [[1,7,3],
        [9,8,2],
        [4,5,6]]

sortMatrix(grid)
