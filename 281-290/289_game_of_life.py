
from typing import List

"""
289. Game of Life (https://leetcode.com/problems/game-of-life/description/)
Follow up: Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

easy solution:
    create a new canvas board called countBoard where countBoard[i][j] stores the number of alive neighbors in board[i][j]
    iterate through board and count the neighbors of each cell to store in countBoard[i][j]
    iterate through board again and update board[i][j] based on the current status and countBoard[i][j]

    runtime = O(n * m)
    space: O(n * m)


better solution: (there's definitely a cleaner way to do this but i don't care)
    we need to store the numbers of alive neighbors for board[i][j] inside of board[i][j] itself
    we also need to store the current status (alive or dead) of board[i][j] as well as the neighbors

    - use a positive or negative sign to state whether board[i][j] is alive 
    - the absolute value will be used to indicate the number of neighbors around each cell

algorithm:
    countAdj(i, j) = number of alive neighbors next to board[i][j]

    1. go through each cell in board and do the following operation:

        if board[i][j] is alive:
            set it's value to (countAdj(i,j) + 2)
                if no alive neighbors, value = 2

        if board[i][j] is dead:
            set it's value to (-2 - countAdj(i, j))
                if no alive neighbors, value = -2

        if we do this, abs(board[i][j])-2 will always contain the number of alive neighbors adjacent to board[i][j]
            we can also distinguish between alive and dead by checking for postive or negative
        i don't actually remember if using -2 and 2 as the base values is significant at all or not maybe using -1 and 1 would work just as fine
    
    2. after processing each cell, go through each cell again and update them based on their values
        for each cell, we know its alive or dead status and also its alive neighbors
        if board[i][j] >= 2, it is alive
        if board[i][j] <= 2, it is dead
        abs(board[i][j]) is the number of neighbors

runtime: O(n*m)
space: O(1) no auxiliary space!!! yipee
"""

def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    n = len(board)
    m = len(board[0])
    directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

    # given any position in board, return whether position is valid to work with
    def inBounds(i, j):
        if i < 0 or j < 0 or i >= n or j >= m:
            return False
        return True


    # given any cell in board, returns the number of live neighbors in eight directions
    def countAdj(i, j):
        count = 0
        for d in directions:
            ii, jj = i+d[0], j+d[1]
            if not inBounds(ii, jj):
                continue
            if board[ii][jj] >= 1:
                count += 1
        return count

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                board[i][j] = countAdj(i, j) + 2 # min value = 2
            else:
                board[i][j] = -1 * countAdj(i, j) - 2 # max value = -2

    for i in range(n):
        for j in range(m):
            curr = board[i][j]
            count = abs(curr) - 2
            if curr >= 2: # alive cell
                if count < 2 or count > 3:
                    board[i][j] = 0
                else: 
                    board[i][j] = 1
            if curr <= -2: # dead cells
                if count == 3:
                    board[i][j] = 1
                else: 
                    board[i][j] = 0


"""
previous solution that uses O(n * m) auxiliary space

runtime: O(n * m)
space: O(n * m)
"""

def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    n = len(board)
    m = len(board[0])
    countBoard = [[0 for _ in range(m)] for _ in range(n)]
    directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

    # given any position in board, return whether position is valid to work with
    def inBounds(i, j):
        if i < 0 or j < 0 or i >= n or j >= m:
            return False
        return True

    # given any cell in board, returns the number of live neighbors in eight directions
    def countAdj(i, j):
        count = 0
        for d in directions:
            ii, jj = i+d[0], j+d[1]
            if not inBounds(ii, jj):
                continue
            if board[ii][jj]:
                count += 1
        return count

    # counting neighbors for each cell in board and storing in countBoard
    for i in range(n):
        for j in range(m):
            countBoard[i][j] = countAdj(i, j)
    
    # updating each value in board in respect to the neighbors in countBoard
    for i in range(n):
        for j in range(m):
            curr = board[i][j]
            count = countBoard[i][j]
            if curr: # live cell
                if count < 2 or count > 3:
                    board[i][j] = 0
            else: # dead cell
                if count == 3:
                    board[i][j] = 1