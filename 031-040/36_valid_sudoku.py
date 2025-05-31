
from typing import List
from collections import defaultdict

"""
36. Valid Sudoku (https://leetcode.com/problems/valid-sudoku/description/)

use three hash sets
    one hash set keeping track of the values seen in each row
    one hash set keeping track of the values seen in each column
    one hash set keeping track of the values seen in each square

every time you see a number record it in the three hash sets
    if a duplicate is found then the sudoku is not valid

math behind the square thing:
    for board[row][col], its square is [row//3][col//3]
    each square will have a different [row//3][col//3] value

algortihm:
    1. create three hash tables rows, columns, and squares
    2. iterate through the 9x9 board
    3. for each cell at board[row][col]
        check that it doesn't exist in rows[row], cols[col], and squares[(row//3, col//3)]
            just hash [row//3][col//3] straight into squares table
    4. if no duplicates found, continue and the values to the corresponding cells

runtime: O(1) always a 9x9 grid - constant time
space: O(1)

"""

def isValidSudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            if (board[row][col] in rows[row]
                or board[row][col] in cols[col]
                or board[row][col] in squares[(row//3, col//3)]):
                return False

            rows[row].add(board[row][col])
            cols[col].add(board[row][col])
            squares[(row//3, col//3)].add(board[row][col])
    return True