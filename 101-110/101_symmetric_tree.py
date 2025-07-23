
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
101. Symmetric Tree (https://leetcode.com/problems/symmetric-tree/description/)
Follow up: Could you solve it both recursively and iteratively?

do a dfs starting with the left root child, record the path taken
do another dfs starting with the right root child, compare the path taken with the first

algorithm:
    1. do a dfs traversal of the tree
    2. start by exploring the left side before exploring the right side for all nodes
    3. record the path taken by this dfs into an array, including null nodes
    4. do another dfs traversal of the tree
    5. this time, start by explorting the right side before exploring the left side for all ndoes
    6. record the path taken by this dfs into another array, including null nodes
    7. compare if the two arrays are identical

runtime: O(n) where n is the size of the tree
space: O(n)

i feel like what i did is very slow but i'll accept this solution
"""

def isSymmetric(root: Optional[TreeNode]) -> bool:

    path = []
    def left(root):
        if not root:
            path.append(None)
            return
        path.append(root.val)
        left(root.left)
        left(root.right)
    
    path2 = []
    def right(root):
        if not root:
            path2.append(None)
            return True
        path2.append(root.val)
        right(root.right)
        right(root.left)


    left(root)
    right(root)
    return path == path2
