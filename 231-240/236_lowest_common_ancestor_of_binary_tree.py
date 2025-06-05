
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
236. Lowest Common Ancestor of Binary Tree (https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

this is just a binary tree, NOT a binary search tree
neetcode.io's version of this question involves a bst so you can just easily search for
nodes p and q by going left or right

for this question there is no assumptions to be made about the order of the nodes
so we have to traverse all of them
stop when p and q have been found

algorithm:
    1. check the left and right subtrees of the current node
    2. return current node if at least one of p or q is found
    3. idk what else

runtime: O(n)
space: O(1) no extra space
"""




def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    
    def dfs(root):
        if not root:
            return None
            
        left = dfs(root.left)
        right = dfs(root.right)

        # just return if one of p or q is found
        if root.val == p.val or root.val == q.val:
            return root
        
        # current node is the lowest common ancestor if this is true
        if left and right:
            return root
        
        return left if left else right

    return dfs(root)