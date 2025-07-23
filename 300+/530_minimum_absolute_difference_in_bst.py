
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
530. Minimum Absolute Difference in BST (https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150)
Note: This question is the same as 783. Minimum Distance Between BST Nodes
    it's literally the same question you can copy paste the solution
    idk who let this happen

important thing to note:
- an in-order traversal (path taken by depth first search left to right), traverses a BST in sorted order

with this information we can just do a dfs and compare each current node with the previous node
return the minimum difference between curr and prev seen

algorithm:
    1. explore as much as you can to the left before doing anything
    2. set prev to = value of the leftmost leaf node 
    3. as you go back up the tree, you are comparing each node to it's left node in sorted order
    4. explore right nodes when you can as you recurse back up
    5. at each recursive case, check current node.val-prev to get the difference between the two
        keep track of the minimum difference seen between any pair of adjacent node values

runtime: O(n) where n is the number of nodes in the tree
space: O(h) where h is the height of the tree
"""

def getMinimumDifference(root: Optional[TreeNode]) -> int:
    minDiff = 1000000
    prev = -1
    def dfs(root):
        nonlocal minDiff, prev

        if not root:
            return
        
        dfs(root.left)
        if prev != -1:
            minDiff = min(minDiff, root.val-prev)

        prev = root.val
        dfs(root.right)
    
    dfs(root)
    return minDiff


        
