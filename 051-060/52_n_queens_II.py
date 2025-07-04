

"""
52. N-Queens II (https://leetcode.com/problems/n-queens-ii/description/)

dawg this is the exact same problem as the first n queens (https://leetcode.com/problems/n-queens/description/)
idk why this problem even exists

in the first question already calculated all possible solutions and returned the solutions themselves in the form of 2d arrays
literally giving us less work by only returning the count for this problem

runtime: O(n!) generates all possible permutations of queen placements with pruning
    first row: n choices, second row: (n-1) choices, third row: (n-2) choices..... = n! choices
space: O(n^2) storing the nxn board at all times 
"""


def totalNQueens(n: int) -> int:
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
    

    res = 0
    def dfs(queens): # returns the grid
        nonlocal res
        # try every possible area in the board
        # add a queen and 
        # backtrack when done

        # base case: i do not know
        if queens == n:
            # return the grid
            res += 1
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