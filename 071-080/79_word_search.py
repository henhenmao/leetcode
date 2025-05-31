
from typing import List

"""
79. Word Search (https://leetcode.com/problems/word-search/description/)

algorithm:
    1. traverse the list and look for the first character of the target word
    2. if first character is found, begin a dfs search starting at that character
        starting at that position, will look in every adjacent direction and check if the next letter exists
        dfs will search for adjecent second, third, fourth character etc.
        a visited 2d array will be used to make sure we don't go back to letters already seen
        if a single letter is missing: dfs stops
    3. if the dfs makes it to the end of the word, returns true
    4. if the list is fully traversed without finding a word: returns false

runtime: O(n^2)
space: O(n^2) a visited array is used

"""

def exist(board: List[List[str]], word: str) -> bool:
    n, m = len(board), len(board[0])
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(word, i, j):
        if len(word) == 0:
            return True
        for d1, d2 in directions:
            a = i + d1
            b = j + d2

            if a < 0 or a >= n or b < 0 or b >= m or visited[a][b]:
                continue
            
            if board[a][b] != word[0]:
                continue
            
            visited[a][b] = True
            if dfs(word[1:], a, b):
                return True
            visited[a][b] = False
        return False
    
    res = False
    for i in range(n):
        for j in range(m):
            if board[i][j] != word[0]:
                continue
            visited[i][j] = True
            res = dfs(word[1:], i, j)
            visited[i][j] = False

            if res:
                return True
    return False