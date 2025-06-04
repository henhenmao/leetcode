
from typing import List
from collections import deque

"""
947. Most Stones Removed with Same Row or Column (https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/)

idea:
    create a graph out of the nodes 
    traverse the graph to find the longest path between any two stones

    this can be treated like the max island area question
        instead of looking for directly adjacent nodes, we look for nodes that share a row or column
    
    i'm gonna crash out
    this doesn't work because there are multiple "islands"
        and the remaining stones from two different islands can form an island 
    entire algorithm falls apart because of this
    
    this question disgusts me


"""

# breath first search to find the largest island
def removeStones(stones: List[List[int]]) -> int:
    
    def isAdjacent(i, j, ii, jj):
        if i == ii or j == jj:
            return True
        return False

    # first get the length and width of the smallest grid possible given the coordinates
    n = max(i[0] for i in stones)+1
    m = max(i[1] for i in stones)+1

    grid = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in stones:
        grid[x][y] = 1

    # for row in grid:
    #     print(row)

    res = 0
    def bfs(i, j):
        nonlocal res
        temp = 1

        queue = deque([[i, j]]) # (i, j) pairs
        while queue:
            x, y = queue.popleft() # (x, y) pair
            for k in range(m): # get each grid[x][k] in the row
                if grid[x][k] == 0 or (k == y):
                    continue
                queue.append([x, k])
                grid[x][k] = 0
                temp += 1

            for k in range(m): # get each grid[k][y] in the row
                if grid[k][y] == 0 or (k == x):
                    continue
                queue.append([k, y])
                grid[k][y] = 0
                temp += 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                grid[i][j] = 0
                bfs(i, j)
    return res-1
                    




stones = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
print(removeStones(stones))