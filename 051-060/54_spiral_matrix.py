

from typing import List

"""
54. Spiral Matrix (https://leetcode.com/problems/spiral-matrix/description/?envType=problem-list-v2&envId=oizxjoit)

idea upon first 5 seconds of viewing problem:
    just move in a striaght line starting right
    when a boundary is reached (out of bounds or visited), change your direction to the right of current direction
    right -> down -> left  -> up

since question states -100 <= matrix[i][j] <= 100, we can mark the visited cells with a number like -101 or 101

given x and y as the horizontal and vertical velocities, four possible directions
    - (0, 1), (1, 0), (0, -1), (-1, 0)

    
algorithm:
    1. start by moving to the right until you reach out of bounds
    2. add each visited cell to the result and change each cell's value to 101 
    3. when you reach out of bounds or encounter a cell marked as 101, change direction to move right of where you are looking
    4. continue until both the cell in front and to the right of you are visited

runtime: O(n * m) where n x m is the size of the matrix
space: O(n * m) to store the result
"""

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    n = len(matrix)
    m = len(matrix[0])

    # function below checks if a position is out of bounds or already visited
    # visited cells will be marked with a value of 101
    def inBounds(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or matrix[i][j] >= 101:
            return False
        return True
        
    # increment to the next direction when an obstacle is encountered

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    i = 0
    j = 0
    k = 0
    res = []
    
    # continue moving forward until there is an obstacle in front and to the right
    while True:
        res.append(matrix[i][j])
        matrix[i][j] = 101 # mark current cell as visited

        curr = directions[k]
        next_i = i + curr[0]
        next_j = j + curr[1]

        if inBounds(next_i, next_j):
            i = next_i
            j = next_j
            continue
        
        k = (k+1)%4
        curr = directions[k]

        next_i = i + curr[0]
        next_j = j + curr[1]

        if inBounds(next_i, next_j):
            i = next_i
            j = next_j
            continue

        break
    
    # print(res)


        


# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# spiralOrder(matrix)
