
"""
168. Excel Sheet Column Title (https://leetcode.com/problems/excel-sheet-column-title/)

the excel sheet column title behaves similarly to a base 26 numbering system so we can just do the following:
    1. get the mod 26
        the mod 26 is the value of the next letter we want to add for the column title id
    2. divide by 26 if we can
        allows us to move on to the next letter

runtime: O(log_26(n)) ??? since we are dividing by 26 each time
space: O(log_26(n))

"""

def convertToTitle(columnNumber: int) -> str:
    res = []

    while columnNumber > 0:
        columnNumber -= 1
        temp = columnNumber % 26
        res.append(chr(ord('A') + temp))
        columnNumber //= 26

    return "".join(res[::-1])

# columnNumber = 3
# print(convertToTitle(columnNumber)) # C
# columnNumber = 27
# print(convertToTitle(columnNumber)) # AA