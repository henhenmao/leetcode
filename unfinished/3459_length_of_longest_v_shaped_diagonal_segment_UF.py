

from typing import List

"""
3459. Length of Longest V-Shaped Diagonal Segment (https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/description/?envType=daily-question&envId=2025-08-27)

V shaped diagonal
    - starts at a 1 cell
    - follows the sequence 2, 0, 2, 0, 2....
    - goes in one diagonal direction and makes at most one turn to a new diagonal direction

dp state
    - current row - 500
    - current col - 500
    - turn made -> 2
    - current direction -> 4

dp[i][j][d][k] will represent the longest V-shaped diagonal starting at the given state
    where i, j is the grid location, k is whether or not a turn is made, and d is the direction index
worst case dp table will be 500 * 500 * 2 * 4 = 2,000,000

- start dfs from every 1 cell in the grid
    - try each direction from each starting point
- follow the 2 0 2 0 alternating sequence 
    - allow one single change of direction


"""

def lenOfVDiagonal(grid: List[List[int]]) -> int:
    def dfs(i, j, currDir, turnMade, dp, currLength, d):
        # base case: if out of bounds or two turns made
        


        # starting at cell 1 and going in direction at index d
        currDir = directions[d]



    n, m = len(grid), len(grid[0])
    directions = [[1,1], [1,-1], [-1,1], [-1,-1]]
    dp = [[[[-1 for _ in range(2)] for _ in range(4)] for _ in range(m)] for _ in range(n)] # absolutely disgusting





