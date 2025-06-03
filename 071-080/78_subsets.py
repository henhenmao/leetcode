
from typing import List

"""
78. Subsets (https://leetcode.com/problems/subsets/)

approaching this question:
    for the first element of the list, we can split into two different possibilities:
        1. you add the element to the subset
        2. you don't add the element to the subset
    this goes for every single element in the list
    we can do this with recursive dfs and backtracking

dfs algorithm:
    1. for each element in nums, recurse without adding the current element
    2. recurse with adding the current element
    3. if you have come across all element of the list (come across, not added to subset), exit the recursion

runtime: O(2^n)
space: O(n) sub contains a max of n values
"""

def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    sub = []    
    def dfs(i):
        if i >= len(nums):
            res.append(sub[:])
            return

        # don't append timeline
        dfs(i+1)

        # append timeline
        sub.append(nums[i])
        dfs(i+1)
        sub.pop() # backtrack

    dfs(0)
    return res