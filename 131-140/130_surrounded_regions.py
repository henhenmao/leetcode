
from typing import List
from collections import deque

"""
130. Surrounded Regions (https://leetcode.com/problems/surrounded-regions/description/)

upon looking at this question for 60 seconds i have the slightest idea of an algorithm
i'm pretty sure there are only two conditions for an O cell to not be surrounded
    1. is touching the edge
    2. is touching another O that is touching the edge
 
as long as this is true, we can just breadth first search from all O cells in the border to mark all non-surrounded O cells

wow it actually worked

algorithm:
    1. traverse the first row, last row, leftmost column, and rightmost column of the board
        add any O cells to the queue and mark the positions in a visited array
    2. do a bfs from the initial bordering O cells to find any connecting O cells
    3. after bfs, compare the visited matrix and the board
        any O cell marked as visited is immune to being surrounded
    4. for each position [i][j] in board and visited matrices, if board[i][j] is an O and visited[i][j] is False:
        the O is surrounded and you can update the cell to be an X        

runtime: O(n * m) where n * m is the size of the matrix
space: O(n * m) visited board
"""

def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    n = len(board)
    m = len(board[0])

    # directions and visited and inBounds for bfs later
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    def inBounds(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return True


    # add all bordering O's to a queue
    queue = deque([])
    for j in range(m): # first and last rows
        if board[0][j] == "O":
            queue.append([0, j])
            visited[0][j] = True
        if board[n-1][j] == "O":
            queue.append([n-1, j])
            visited[n-1][j] = True
            
    for i in range(1, n-1): # leftmost and rightmost columns
        if board[i][0] == "O":
            queue.append([i, 0])
            visited[i][0] = True
        if board[i][m-1] == "O":
            queue.append([i, m-1])
            visited[i][m-1] = True

    
    # do bfs to find all O cells connected to bordering O
    while queue:
        i, j = queue.popleft()

        for x, y in directions:
            next_i = i+x
            next_j = j+y
        
            if not inBounds(next_i, next_j) or visited[next_i][next_j] or board[next_i][next_j] == "X":
                continue

            visited[next_i][next_j] = True
            queue.append([next_i, next_j])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "O" and not visited[i][j]:
                board[i][j] = "X"
    
    
# board = [["X","X","X","X"],
#          ["X","O","O","X"],
#          ["X","X","O","X"],
#          ["X","O","X","X"]]
# solve(board)
# for row in board:
#     print(row)
