


"""
62. Unique Paths (https://leetcode.com/problems/unique-paths/description/)

finding the number of paths from a given cell at [i][j]:
    for each cell at [i][j], there are two different possibilities:
        1. go down (if possible)
        2. go right (if possible)
    the total number of possibilities from cell [i][j] is simply the sum of the two possibilities
        [i][j] = [i+1][j] + [i][j+1]

algorithm:
    we will use a dp table to tabulate all results starting from the end and making our way to the top
    [0][0] will be the end and [n-1][m-1] will be the beginning
        (the question states the grid is m x n but i swapped them)
    we are trying to find the total number of possibities at the beginning cell

    1. create a n x m dp table and set dp[0][0] to 1 (so you have something to build off of)
    2. do a double loop to traverse each cell in the grid
    3. for each cell, check the cell on top and the cell to the left of it
        this is essentially checking the possibility of moving right and moving down in the question
        if cells are out of bounds just don't count it
    4. set the current cell as the sum of the cell above and to the left
    5. once loops are done, dp[n-1][m-1] will have the total possibilities from the start, return

    
runtime: O(n * m)
space: O(n * m)
"""


def uniquePaths(n: int, m: int) -> int:
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1

    def inBounds(x, y):
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        return True

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            left = dp[i][j-1] if inBounds(i, j-1) else 0
            top = dp[i-1][j] if inBounds(i-1, j) else 0
            dp[i][j] = left+top
    return dp[-1][-1]