

from typing import List
from collections import deque

"""
417. Pacific Atlantic Water Flow (https://leetcode.com/problems/pacific-atlantic-water-flow/description/?envType=problem-list-v2&envId=oizxjoit)

idea:
    start with adding all values in the border in a queue
    create a visited array and mark all elements in the queue to be marked
        for each visited[i][j], have two boolean values for whether or not heights[i][j] can reach the pacific or can reach the atlantic
    
    maybe do two separate bfs with two queues: one with pacific bordering cells and one with atlantic bordering cells
    then do a standard bfs with the initial elements in the queue

algorithm:
    1. create a n*m visited array containing two booleans each cell [can access pacific, can access atlantic]
    2. get all cells that are touching the pacific and add them to a pacfiic queue
        mark the positions in the visited array (visited[i][j][0] = True)
    3. do the same thing for the atlantic touching cells
    4. for each of the pacific and atlantic arrays, do a bfs to mark all adjacent values that can be accessed
        since we are starting from the edges, we only access heights that are larger or equal to the current height in the bfs
    5. iterate through all cells in the array and check for cells marked [True, True]
        cells marked with that means touching both oceans

runtime: O(n * m) where n * m is the size of the matrix
space: O(n * m)

there are many optimization things i could do to make this much muhc faster but i dont want to
"""

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    n = len(heights)
    m = len(heights[0])

    def inBounds(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return True
    
    directions = [[0,1],[1,0],[0,-1],[-1,0]]

    pacific = deque([])
    atlantic = deque([])
    visited = [[[False, False] for _ in range(m)] for _ in range(n)] # {pacific, atlantic}

    # get all values that are initially touching the pacific
    # do the same for the atlantic
    # do the same for the corners

    # starting with the pacific cells
    for j in range(1, m):
        visited[0][j][0] = True
        pacific.append([0, j])
    for i in range(n):
        visited[i][0][0] = True
        pacific.append([i, 0])
    
    # add atlantic cells
    for j in range(m-1):
        visited[-1][j][1] = True
        atlantic.append([n-1, j])
    for i in range(n):
        visited[i][-1][1] = True
        atlantic.append([i, m-1])

    # use pacific and atlantic arrays for two separate bfs and mark cells with True for the respective oceans
    # pacific bfs:
    while pacific:
        i, j = pacific.popleft()
        for d in directions:
            next_i = i + d[0]
            next_j = j + d[1]

            # only consider heights that are equal to or higher than the current height
            # also onyl consider heights that haven't been marked
            if not inBounds(next_i, next_j) or visited[next_i][next_j][0] or heights[next_i][next_j] < heights[i][j]:
                continue

            visited[next_i][next_j][0] = True
            pacific.append([next_i, next_j])
    
    # now do the same thing for atlantic array bfs:
    while atlantic:
        i, j = atlantic.popleft()
        for d in directions:
            next_i = i + d[0]
            next_j = j + d[1]

            if not inBounds(next_i, next_j) or visited[next_i][next_j][1] or heights[next_i][next_j] < heights[i][j]:
                continue

            visited[next_i][next_j][1] = True
            atlantic.append([next_i, next_j])

    res = []
    for i in range(n):
        for j in range(m):
            if visited[i][j] == [True, True]:
                res.append([i, j])
    return res


# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# heights = [[1]]
# print(pacificAtlantic(heights))