
from typing import List

"""
212. Word Search II (https://leetcode.com/problems/word-search-ii/description/)

take the same word search algorithm from the first word search question
    use a prefix tree to backtrack early if the current string of words doesn't exist for any word

- build a prefix tree from the list of words
- do the same word search dfs algorithm in the first word search

algorithm:
    1. create prefix tree containing each word in words
    2. starting at the root node, for each cell on the board, check that the current character is a child of the current node
        if not a child, return since this path is useless
    3. check if current character is an ending character that completes a word in words
        if true, add the  word + cell to the result array
            to avoid duplicates, set the trie node you are at to false
    4. mark the current cell of the board as a # to mark the cell as visited for this recursive path
        so that the same cell isn't repeated for a word search path
    5. recurse into each of the four adjacent cells from the current board cell

n, m = size of board
k = number of words
l = average length of each word

runtime:
    time of building the trie = O(k * l)
    time of word search dfs = O(n * m * k)
    total runtime: O(n * m * k + k * l)

space: O(n * m + k * l)

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

def findWords(board: List[List[str]], words: List[str]) -> List[str]:

    # create a prefix tree of the words
    root = TrieNode()

    # adding each word into the prefix tree
    for word in words:
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True


    n, m = len(board), len(board[0])
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    res = []

    def dfs(word, i, j, curr):
        cell = board[i][j]

        if cell not in curr.children:
            return
        
        next = curr.children[cell]

        if next.end:
            res.append(word+cell)
            next.end = False
            
        board[i][j] = "#" # marked as visited
        for d1, d2 in directions:
            a = i + d1
            b = j + d2
            
            if a < 0 or a >= n or b < 0 or b >= m or board[a][b] == "#":
                continue

            dfs(word+cell, a, b, next)

        board[i][j] = cell # unmark visited cell


    for i in range(n):
        for j in range(m):
            dfs("", i, j, root)
            
    return res


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oa", "oaa"]

print(findWords(board, words))