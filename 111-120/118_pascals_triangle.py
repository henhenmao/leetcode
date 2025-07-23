
from typing import List

"""
118. Pascal's Triangle (https://leetcode.com/problems/pascals-triangle/description/)

i just iteratively created by row by adding the previous row values
i do not know if there is a linear solution but there might be

algorithm:
    1. start with a single row of [1]
    2. for each pair of values in the previous row, append their sum into the new row
    3. add a 1 in the beginning and end of the new row
    4. add the new row into the total triangle

runtime: O(n^2)
space: O(n^2)
"""

def generate(numRows: int) -> List[List[int]]:
    res = [[1]]
    for _ in range(numRows-1):
        # add in pairs to create new row
        newRow = [1]
        for i in range(len(res[-1])-1):
            newRow.append(res[-1][i] + res[-1][i+1])
        newRow.append(1)
        res.append(newRow)
    return res