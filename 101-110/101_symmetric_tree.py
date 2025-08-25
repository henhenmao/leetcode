
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

recursive algorithm:
    create a helper funciton that takes in two treenodes
    have two roots, one starting at the left child of root and the other at the right child of root
    let root1 = left child and root2 = right child
    at each recursive call, check if root1.left and root2.right are symmetric
        do the same with root1.right and root2.left
    
edge cases:
    no root: return nullptr
    only one child of root: return false
    no children of root: return true

algortihm:
    1. check two edge cases
        return true if root == nullptr or root has no children
    2. recurse in helper with root1=root.left and root2=root.right
    3. if root1 != root2, return false
    4. return recursively into root1.left, root2.right and root1.right, root2.left
    
runtime: O(n) where n is the number of nodes
space: O(log(n))
"""

def isSymmetric(root: Optional[TreeNode]) -> bool:
    def isSymmetricHelper(root1, root2):
        if not root1 or not root2:
            return root1 == root2

        return root1.val == root2.val and isSymmetricHelper(root1.left, root2.right) and isSymmetricHelper(root1.right, root2.left)

    if not root:
        return True
    return isSymmetricHelper(root.left, root.right)


"""
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
"""

