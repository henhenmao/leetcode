
from typing import List

"""
200. Number of Islands (https://leetcode.com/problems/number-of-islands/)

this is one of my favorite questions i just really like it

all land that is adjacent to more land is considered a part of that land and one island

algorithm:
    1. create an n x m visited grid
    2. traverse the grid with double loop
        if land is discovered, use a dfs to explore all land connecting to that piece of land
        mark all discovered pieces of land as visited
    3. continue to traverse the grid as you skip already discovered land and water (0)

runtime: O(n * m)
space: O(n * m)
"""

def numIslands(grid: List[List[str]]) -> int:
    directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
    n = len(grid)
    m = len(grid[0])

    def dfs(i, j):
        nonlocal grid

        for d in directions:
            a = i+d[0]
            b = j+d[1]
            if a < 0 or a >= n or b < 0 or b >= m:
                continue
            if grid[a][b] == "1" and not visited[a][b]:
                visited[a][b] = True
                dfs(a, b)
    
    # have a visited 2D array 
    # loop through each element in the graph
    # each 1 is a potential dfs call
    # if 1 is encountered: add 1 to the result and mark each adjacent island in the visited graph

    visited = [[False for _ in range(m)] for _ in range(n)]
    islands = 0

    for i in range(n):
        for j in range(m):

            if grid[i][j] == "0" or visited[i][j]:
                continue

            # all conditions are met
            islands += 1
            visited[i][j] = True
            dfs(i, j)

    return islands