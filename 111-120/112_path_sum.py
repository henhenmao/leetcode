
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
112. Path Sum (https://leetcode.com/problems/path-sum/description/)

we know we are at a leaf node when there are no children
    we can just check if not root.left and not root.right for no children on both ends
        if a leaf node is verified, we can check if the current path sum adds up to total

use a standard binary tree dfs traversal to find all paths from the root node to all leaf nodes
    keep track of the current sum on each path by having a target parameter and add all encoutnered values to it
    
    when a leaf node is found, check if target == targetSum:
        if true: you have found your path and can return true
        if false: keep looking lmao

algorithm:  
    1. base case: if node is null, return
    2. check if current node is a leaf node (both children are null)
    3. if leaf node, check if your current sum is equal to the target sum, return true if true
    4. continue the dfs into children if children exist

runtime: O(n) where n is the size of the tree
space: O(n)
"""


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    def dfs(root, target):
        if not root:
            return False
        if not root.right and not root.left:
            return target+root.val == targetSum
        return dfs(root.left, target+root.val) or dfs(root.right, target+root.val)
    return dfs(root, 0)