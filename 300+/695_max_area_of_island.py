

from typing import List
from collections import deque

"""
695. Max Area of Island (https://leetcode.com/problems/max-area-of-island/description/)

the island questions always use breadth first search for probably a reason

algorithm: 
    1. traverse the grid
    2. if a 1 is encountered, begin a breadth first search starting there
    3. use the bfs to explore all connecting 1s to the first cell
    4. mark all visited 1s as 0s so they don't get checked again
    5. at the end of the bfs see if the total area of your island is greater than the current max

runtime: O(n * m)
space: O(n * m)
"""



def maxAreaOfIsland(grid: List[List[int]]) -> int:
    
    # breath first search to find the largest island

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n = len(grid)
    m = len(grid[0])
    max_area = 0


    def bfs(i, j):
        nonlocal max_area

        q = deque([[i, j]])
        temp = 1

        while q:
            curr = q.popleft()
            for dr, dc in directions:
                a = curr[0] +dr
                b = curr[1] +dc
                if a < 0 or a >= n or b < 0 or b >= m or grid[a][b] == 0:
                    continue
                
                q.append([a, b])
                grid[a][b] = 0
                temp += 1
        if temp > max_area:
            max_area = temp

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                grid[i][j] = 0
                bfs(i, j)
        
    return max_area