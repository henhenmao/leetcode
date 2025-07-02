
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
257. Binary Tree Paths (https://leetcode.com/problems/binary-tree-paths/description/)

a leaf is a node with no children
to get all root to leaf paths, do a dfs traversal from the root node to get all paths from the root node
to know when a leaf node is encountered and should end the path, check if current node has no children
    if zero children, add path to the result and end path
    if one child, continue dfs down that single path
    if both children, continue dfs down both paths

runtime: O(n) where n is the number of n
space: O(n)
"""

def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    allPaths = []
    def dfs(root, path):
        path += str(root.val)

        if not root.left and not root.right:
            allPaths.append(path)
            return
    
        if root.left:
            dfs(root.left, path+"->")
        if root.right:
            dfs(root.right, path+"->")

    dfs(root, "")
    return allPaths