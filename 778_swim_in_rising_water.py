

from typing import List
import heapq

"""
778. Swim in Rising Water (https://leetcode.com/problems/swim-in-rising-water/description/?envType=daily-question&envId=2025-10-04)

do something similar to dijkstras algorithm but instead of keeping track of weights, keep track of the maximum value along the path
    we are basically just finding the path from (0,0) to (n-1, n-1) where the maximum value along the path is minimized
    for this question, the time it takes to travel along any path on the grid is equal to the maximum value along that path
        remember that the question states that "you can travel an inifinite distance in zero time" as long as each cell is reachable

i just learned that python support chained comparison operations so i can do if i == j == n-1 without doing two separate if statements

1.  

"""

def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    visited = [[False for _ in range(n)] for _ in range(n)]
    directions = ((1,0),(-1,0),(0,1),(0,-1))
    pq = [(grid[0][0], 0, 0)]
    max_time = 0

    while pq:
        curr_height, i, j = heapq.heappop(pq)

        if visited[i][j]:
            continue
        visited[i][j] = True

        max_time = max(max_time, curr_height)

        if i == j == n-1: # end of path reached
            return max_time
        
        for x, y in directions:
            next_i, next_j = i+x, j+y
            if 0 <= next_i < n and 0 <= next_j < n and not visited[next_i][next_j]:
                heapq.heappush(pq, (curr_height, next_i, next_j))
    
    return max_time # this line should never run in a normal case
     










grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(swimInWater(grid))