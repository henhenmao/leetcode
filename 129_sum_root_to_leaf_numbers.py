
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
129. Sum Root to Leaf Numbers (https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)

algorithm:
    1. use dfs to travel along every root to leaf path
    2. as you go along the way build a string of all of the digits you go across
    3. when the leaf of the path is reached, convert the built string into integer and add to the total
        leaf is only reached when current node has no left children AND no right children
        keep going as long as one child still exists

runtime: O(n) where n is the number of nodes
space: O(n)
"""

def sumNumbers(root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(root, curr):
        nonlocal res
        curr += str(root.val)

        if not root.left and not root.right:
            res += int(curr)
            return
        
        if root.left:
            dfs(root.left, curr)
        if root.right:
            dfs(root.right, curr)

    dfs(root, "")
    return res
        