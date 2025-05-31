
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
226: Invert Binary Tree (https://leetcode.com/problems/invert-binary-tree/description/)

like most binary tree problems, this can be solved using recursive dfs

inverting binary tree:
    to "invert" a binary tree means to swap the left and right children of each node in the tree
    swapping left and right can easily be done with
        root.left, root.right = root.right, root.left

algorithm:
    1. at each node, swap the left and right node
    2. recurse into the left and right nodes so you can swap the children of those nodes as well
    3. stop recursion when you reach the end of the tree (no children in the node)

runtime: O(n) where n is the number of nodes in the tree
space: O(1)
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root