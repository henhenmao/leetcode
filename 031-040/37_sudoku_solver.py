
from collections import defaultdict
from typing import List

"""
37. Sudoku Solver (https://leetcode.com/problems/sudoku-solver/)
It is guaranteed that the input board has only one solution.

should try every possible digit for any given cell while keeping track of the row and column and square with hash sets
backtrack if a number is incompatible

since we are using a depth first search backtracking algorithm to look for a single solution:
    set the condition that finds the solution to return true
    we keep returning the recursive calls until a recursive call returns true
    this allows us to stop the algorithm when the solution is found and avoids unnecessary recursive calls

solution condition:
    since we know that the sudoku board is 9x9 = 81 cells, we can subtract the initial cells of the input
    to get the number of cells left that we need to fill in

algorithm:
    1. traverse the board to see all initial cells in the sudoku
        - add initial cells into the row, col, and square sets
        - set a count = 81 and subtract count by one every time an initial cell is found
    2. begin the depth first search traversal
    3. for each empty cell in the current call, try every digit from 1-9
        check if the digit already exists in the same row, col, or square by checking the sets
    4. if digit is valid to place in the board
        - add digit to the board
        - add digit to each of the sets
        - subrtact the count by 1
    5. backtrack after recursing
        - remove digit from board
        - remove digit from the sets
        - increase count by 1
    6. base case: count = 0
        if count = 0, we know that the board has been completely filled out with no issues
        we can simply return true after finding solution

runtime: O(9^n) where n is the number of empty cells in the input - i have no idea what the runtime is this is just a guess
space: O(1) no extra space is used
"""

def solveSudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)
    count = 81

    # mark the initial sudoku values in the sets
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            
            rows[row].add(int(board[row][col]))
            cols[col].add(int(board[row][col]))
            squares[(row//3, col//3)].add(int(board[row][col]))
            count -= 1

    # print(count)

    def backtrack(i, j):
        nonlocal count

        if i == 9:
            return True

        # reached end of current row, move to the next row
        if j == 9:
            return backtrack(i + 1, 0)

        # base case
        if count == 0: # all cells filled
            return True
        
        # move to the next cell if current one is already filled
        if board[i][j] != ".":
            return backtrack(i, j+1)
        
        for digit in range(1, 10):
            if (digit in rows[i] or digit in cols[j] or digit in squares[(i//3, j//3)]):
                continue
            
            # try digit and backtrack
            board[i][j] = str(digit)
            rows[i].add(digit)
            cols[j].add(digit)
            squares[(i//3, j//3)].add(digit)
            count -= 1

            # stop and return if solution is found
            if backtrack(i, j+1):
                return True
            
            board[i][j] = "."
            rows[i].remove(digit)
            cols[j].remove(digit)
            squares[(i//3, j//3)].remove(digit)
            count += 1
        return

    backtrack(0, 0)



# board = [["5","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]]
# solveSudoku(board)

# for row in board:
#     print(row)


