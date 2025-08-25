
from typing import List

"""
498. Diagonal Traverse (https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25)

traversing diagonally
    from a starting location at mat[i][j], you can move diagonally by either incrementing or decrementing both i and j
    continue to move in the same diagonal direction
        if the edge of the matrix is reached, change the diagonal direction
    notice how the specific traversal for this question only involves going up-right or down-left
        so we just swap between these two directions every time an edge is reached

finding the next direction:
    if initially moving up-right and edge is reached:
        if there is a cell directly to the right, go there
        if there is not a cell directly to the right, go down
    if initially moving down-left and edge is reached:
        if there is a cell directly downwards, go there
        if there is not a cell directly downwards, go right

    the reason you can't just do the same thing for both directions is because
        you have to check the right cell first if you are moving up-right
        have to check the downward cell first if you are moving down-left

algorithm:
    1. starting at mat[0][0] and currently going up-right
        continue to go in that direction until an edge is reached, add all cells to a list
    2. when an edge is reached
        if you are currently going up-right, you either need to go to the right cell or the downward cell, only one will exist i think
            first check if the right cell exist, move to the right if it exists, else move down
        if you are currently going down-left, you either need go to the downward cell or right cell
            first check if the down cell exists, move down if ti exists, else move right
        swap your direction between the two directions afterwards
    3. continue until you reach the last cell at mat[m-1][n-1]

runtime: O(m * n)
space: O(m * n)
"""


def findDiagonalOrder(mat: List[List[int]]) -> List[int]:

    def inBounds(x, y, m, n):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        return True


    path = []
    dirs = [[-1, 1], [1, -1]]
    curr_dir = 0

    m, n = len(mat), len(mat[0]) # m = num rows, n = num cols
    i, j = 0, 0 # starting position of traversal


    while i != m and j != n:
        # adding the current cell to the path
        path.append(mat[i][j])

        next_i = i + dirs[curr_dir][0]
        next_j = j + dirs[curr_dir][1]

        # keep going in same direction if cell available
        if inBounds(next_i, next_j, m, n):
            i = next_i
            j = next_j
            continue
    
        # find new direction if cannot move any further

        if curr_dir == 0: # currently going up-right
            if inBounds(i, j+1, m, n): #
                j += 1
            else:
                i += 1
        
        else: # currently going down-left
            if inBounds(i+1, j, m, n):
                i += 1
            else:
                j += 1

        curr_dir = (curr_dir+1)%2

    return path


mat = [[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(mat))