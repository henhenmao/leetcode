
from typing import List


"""
90. Subsets II (https://leetcode.com/problems/subsets-ii/)

can possibly use a hash set to keep track of the used integers for each recursed subarray 

can also sort the array and just skip duplicates when iterating
    sorting doesn't really matter since its gonna be in O(2^n) time anyways
    very similar to 40. Combination Sum II

at each nums[i], we can either append it to our subset or not append it to the subset and then recurse as usual
the only difference is that we want to skip duplicates in the same recursive call
as long as the initial nums is sorted, we can skip duplicates in the same recursive call by skipping cases where nums[i] == nums[i+1]    

algorithm:
    1. append nums[i] the subset and recurse into the case where we add nums[i] to the subarray
    2. backtrack by popping from the subset
    3. to skip duplicates, we can increase i until nums[i] does not equal nums[i+1]
    4. recurse into the case where we don't add nums[i] to the subarray
    5. base case: add current subset to result when all elements in i have been traversed recursively

runtime: O(n * (2^n)) we go through a max of 2^n possibilities for each element and then copy the subset into res in O(n)
space: O(n) curr contains a max of n values

"""

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    def dfs(i, curr):
        if i >= len(nums):
            res.append(curr[:])
            return


        curr.append(nums[i])
        dfs(i+1, curr)
        curr.pop()
        
        # skipping duplicates
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        
        dfs(i+1, curr)
        return

    dfs(0, [])
    return res