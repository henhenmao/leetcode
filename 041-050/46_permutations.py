
from typing import List

"""
46. Permutations (https://leetcode.com/problems/permutations/description/)

standard dfs and backtracking algorithm used for permutations 

dfs algorithm:
    1. loop through each number in nums
    2. for each value nums[i], recurse through the possibility of adding nums[i] to the result
    3. backtrack and remove nums[i] from the result because of the possibility of not adding nums[i] to the result
    4. once dfs is over it should have covered all of the possible permutations

runtime: O(n! * n) where n is the length of nums, there are n! permutations where you do up to O(n) word due to splicing
space: O(n! * n) 

this is very slow :(
"""


def permute(nums: List[int]) -> List[List[int]]:
        
    res = [] # storing all of the permutations

    def dfs(nums, curr): # curr is current building permutation

        # base case: append permutation and return when all nums are used
        if len(nums) == 0:
            res.append(curr[:])
            return 

        # loop through each value in nums
        # and remove it from nums when used
        # backtrack it back into nums when the dfs is done 
        for i in range(len(nums)):
            curr.append(nums[i])

            temp = nums[:i] + nums[i+1:] # remove currently selected element from nums

            dfs(temp, curr) # recursively iterate

            curr.pop() # backtrack added num back to nums
            
    dfs(nums, [])
    return res