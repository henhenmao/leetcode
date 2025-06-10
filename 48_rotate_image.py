

from typing import List

"""
48. Rotate Image (https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=oizxjoit)
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

how to rotate a matrix by 90 degrees clockwise:
    you can rotate a matrix by doing transformations on the matrix, mainly reflections
    if we reflect the matrix along the y-axis, and then reflect the matrix along the y = x diagonal line
        we get a matrix rotated 90 degrees clockwise
    reflecting in the y = -x diagonal can also get us a counter clockwise 90 degree rotation


alorithm:
    1. reflect matrix along y axis by performing swaps 
    2. reflect matrix along y = x line by performing swaps
    3. boom the matrix is reflected

runtime: O(n * m) where n and m are the length and width of the matrix probably
space: O(1) 

"""


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    n = len(matrix)
    m = len(matrix[0])

    # function that swaps the cells at matrix[a][b] and matrix[x][y]
    def swap(a, b, x, y):
        matrix[a][b], matrix[x][y] = matrix[x][y], matrix[a][b]

    # reflect the matrix along the y-axis
    for i in range(n):
        for j in range(m//2):
            swap(i, j, i, n-j-1)
    
    # reflect the matrix along the y = x line
    # giving us a 90 degree clockwise rotation
    for i in range(n):
        for j in range(m-i-1):
            swap(i, j, n-j-1, m-i-1)

            # print([i, j])
            # print([j, i])


# for row in matrix:
#     print(row)

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# rotate(matrix)