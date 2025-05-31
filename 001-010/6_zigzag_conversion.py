

"""
6. Zigzag Conversion (https://leetcode.com/problems/zigzag-conversion/description/)

things to note for this question:
    you will reach the bottom row of the zigzag pattern when moving straight down
    you will reach the top row of the zigzag pattern when going diagonally up
    you begin the pattern by going straight down

my solution:
    create a 2d array to store the output, we need numRows rows as output

    only the current row actually changes every increment in the string
    have a variable that tells you your current direction (straight down or diagonally)
        set the variable to straight down at the start

    for every increment, store the current character into the current row and then update to the new row
    
time complexity: O(n) only goes through the input string once
space complexity: O(n) total number of characters stored is the length of the string

"""

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    grid = [[] for _ in range(numRows)]
    row = 0
    zig = True
    i = 0
    
    while i < len(s):
        if zig and row == numRows-1:
            zig = False
        if not zig and row == 0:
            zig = True

        grid[row].append(s[i])
        
        if zig:
            row += 1
        else:
            row -= 1
        i += 1
    
    res = ""
    for row in grid:
        res += "".join(row)
    return res