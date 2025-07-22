
from typing import List

"""
119. Pascal's Triangle II (https://leetcode.com/problems/pascals-triangle-ii/description/)
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

i literally did the same thing from the previous question but returned the row at rowindex

runtime: O(n^2)
space: O(n^2)
"""

def getRow(rowIndex: int) -> List[int]:
    numRows = rowIndex
    res = [[1]]
    for _ in range(numRows):
        # add in pairs to create new row
        newRow = [1]
        for i in range(len(res[-1])-1):
            newRow.append(res[-1][i] + res[-1][i+1])
        newRow.append(1)
        res.append(newRow)
    return res[-1]