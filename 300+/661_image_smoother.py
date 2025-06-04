
from typing import List

"""
661. Image Smoother (https://leetcode.com/problems/image-smoother/description/)

algorithm:
    1. create a (n * m) res array since we need to do calculations without changing img
    2. for each img[i][j], look in all eight directions, check if img[i][j] is in bounds and then get the average of each surrounding cell and current cell
    3. set res[i][j] to the average

runtime: O(n * m) where n is the number of row and m is the number of columns
space: O(n * m)    

"""

def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    
    def inBounds(i, j):
        if i < 0 or j < 0 or i >= n or j >= m:
            return False
        return True

    def smoothCell(i, j):
        count = 0
        cells = 0
        for x, y in directions:
            x += i
            y += j
            if not inBounds(x, y):
                continue
            cells += 1
            count += img[x][y]
        return count//cells
            
    directions = ((-1, -1), (-1, 0), (-1, 1),
                    (0,-1),   (0,0),   (0, 1),
                    (1, -1),  (1, 0),  (1, 1),)

    n = len(img)
    m =  len(img[0])
    res = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            res[i][j] = smoothCell(i, j)
    return res




