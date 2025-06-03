
from typing import List

"""
51. N-Queens (https://leetcode.com/problems/n-queens/)

for any queen on the board, we want to try every board[i][j] on the board
if a queen can be safely placed, we place it and recurse for the next queen

have a function to be able to check whether or not a position at [i][j] is valid or not
    keep track of all positions being attacked by a queen

when a queen at board[i][j] is placed, the following places are invalid:
    - the entire row of i
    - the entire column of j
    - all diagonals to [i][j]
        - how to get diagonals efficiently?

i'm just going to start my code by checking for attacked squares through iteration
    i'm guessing there's a better way using hash sets or something


algorithm:
    1. create function that checks if board[i][j] is being attacked by a queen or not
        checks the row and column and diagonals of board[i][j] for a possible queen
    2. recursive function:
        iterate through the board and keep checking every board[i][j] if you can place a queen there
        is board[i][j] is not being attacked, can place a queen there
            after placing a queen, recurse to the next row and add a queen
    3. after recurse, backtrack and remove the queen you placed and move on with the iteration

runtime: O(n!) generates all possible permutations of queen placements with pruning
    first row: n choices, second row: (n-1) choices, third row: (n-2) choices..... = n! choices
space: O(n^2) storing the nxn board at all times 
"""


def solveNQueens(n: int) -> List[List[str]]:

    board = [["." for _ in range(n)] for _ in range(n)]

    # might not actually need this function but i'm gonna put it here
    def inBounds(x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        return True
    
    # function that checks if board[x][y] is being attacked by other queens or not
    # will write a O(n^2) search that looks at the rows and columns
    def isAttacked(x, y):
        # check rows
        for j in range(n):
            if j != y and board[x][j] == "Q":
                return True

        # check columns

        for i in range(n):
            if i != x and board[i][y] == "Q":
                return True

        # check diagonals
        # i'm just going to check all four directions
        i, j = x-1, y-1
        while inBounds(i, j):
            if board[i][j] == "Q":
                return True
            i -= 1
            j -= 1
        i, j = x+1, y-1
        while inBounds(i, j):
            if board[i][j] == "Q":
                return True
            i += 1
            j -= 1
        i, j = x-1, y+1
        while inBounds(i, j):
            if board[i][j] == "Q":
                return True
            i -= 1
            j += 1
        i, j = x+1, y+1
        while inBounds(i, j):
            if board[i][j] == "Q":
                return True
            i += 1
            j += 1
        return False
    

    res = []
    def dfs(queens): # returns the grid
        # try every possible area in the board
        # add a queen and 
        # backtrack when done

        # base case: i do not know
        if queens == n:
            # return the grid
            res.append(["".join(row) for row in board])
            return        

        # we can use queens as the row index
        # since placing a queen basically moves on to the next row anyways
        for j in range(n):
            if not isAttacked(queens, j):
                board[queens][j] = "Q"
                dfs(queens+1)
                board[queens][j] = "."

    dfs(0)
    return res

# res = solveNQueens(5)
# for grid in res:
#     for row in grid:
#         print(row)
#     print()


