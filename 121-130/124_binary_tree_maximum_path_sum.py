
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
124. Binary Tree Maximum Path Sum (https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

at each node: you have the following choices
    - join together the two separate left and right branches
    - only choose the left branch to connect to the parent
    - only choose the right branch to connect to the parent
    - not choosing either branch and just returning itself

algorithm:
    1. at each node root, recurse into the left and right children (base case reached if no children)
    2. at each node, consider the possibilities
        - join together the two separate left and right branches
        - join left branch to parent
        - join right branch to parent
        - ignoring left and right and just returning itself
    3. return the max of just between the left and right max sums
        we ignore the first case since this is considering the possibility of the path leading to the parent
            which is not possible if you join the left and right branches
        return the max of left and right + current node value

runtime: O(n), where n is the number of nodes in the tree, each node is travelled once
space: O(n)
"""

def maxPathSum(root: Optional[TreeNode]) -> int:
    max_path = -1001
    
    def dfs(root):
        nonlocal max_path
        if not root:
            return 0
        
        left = max(dfs(root.left), 0)
        right = max(dfs(root.right), 0)

        # set max_path
        max_path = max(max_path, left + right + root.val)

        return root.val + max(left, right)

    dfs(root)
    return max_path