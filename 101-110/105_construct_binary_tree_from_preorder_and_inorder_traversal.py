



from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
105. Construct Binary Tree from Preorder and Inorder Traversal (https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

use to iterate through the preorder array
base case: no more elements in the array
1. find the spot in the inorder array to split
2. create the tree node
3. recurse into the left and right side of the split
4. increment to next value in preoder (it should match with the dfs)

note: recurse with pointers on the inorder array instead of recursing with subarrays
    indices get messed up when subarrays are made so it won't work

runtime: O(n) where n is length of preorder and inorder
space: O(n)
"""

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
    # hash the indexes of all elements in inorder array:
    #   both arrays consist of unique values btw
    indices = {}
    for i, node in enumerate(inorder):
        indices[node] = i
    print(indices)

    i = 0
    def dfs(start, end):
        nonlocal i

        # base case: start is greater than end: end of branch
        if start > end:
            return None

        curr = preorder[i]
        i += 1

        root = TreeNode(curr)
        split = indices[curr]
        root.left = dfs(start, split-1)
        root.right = dfs(split+1, end)
        return root

    return dfs(0, len(preorder)-1)