
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



"""


def solveNQueens(n: int) -> List[List[str]]:

    # might not actually need this function but i'm gonna put it here
    def inBounds(x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        return True
    
    # function that checks if board[x][y] is being attacked by other queens or not
    def isAttacked(x, y):
        return


    
    board = [["." for _ in range(n)] for _ in range(n)]
    print(board)


    def queens():
        return


