
from typing import List

"""
463. Island Perimeter (https://leetcode.com/problems/island-perimeter/)

i really like this question something about it makes me feel some sort of way

things to notice:
    - one cell has a perimeter of 4 if it is not touching anything
    - each individual cell loses 1 from its perimeter for each cell it touches

algorithm
    1. loop through each cell in grid
    2. for each piece of land check the four adjacent cells for more land
    3. assume each piece of land has a perimeter of 4 and subtract 1 for each adjacent piece of land
    4. add up the total perimeter

runtime: O(n * m)
space: O(1)
"""

def islandPerimeter(grid: List[List[int]]) -> int:
    def inBounds(x, y, a, b):
        if x < 0 or x >= a or y < 0 or y >= b:
            return False
        return True
    
    directions = ((0, -1), (0, 1), (1, 0), (-1, 0))

    perimeter = 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            for d in directions:
                tempi = i + d[0]
                tempj = j + d[1]
                if not inBounds(tempi, tempj, n, m):
                    continue
                if grid[tempi][tempj] == 1:
                    perimeter -= 1
            perimeter += 4
    return perimeter