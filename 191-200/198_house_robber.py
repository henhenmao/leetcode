
from typing import List

"""
198. House Robber (https://leetcode.com/problems/house-robber/)

at each nums[i] there are two possibilites:
    1. you rob nums[i] and move to nums[i+2]
    2. you don't rob nums[i] and move to nums[i+1]

you simply want to check all possibilities, and compare the possibility that gets you the most money
we can use a dfs to check all possibilities 

since we are checking dfs(i+1) and dfs(i+2), there will be many repeated method calls
because of this, we should memoize the robbed value for each house at nums[i] in a dp table

algorithm:
    1. create a dp table of size n
    2. for each house at nums[i], recurse the values of the following two possibilities:
        robbing nums[i] and skipping next house (nums[i] + dfs(i+2))
        going to next house (dfs(i+1))
    3. compare the two values and memoize the value with more money
    4. dp[0] will contain the total maximum from all houses

runtime: O(n) where n is the length of nums
space: O(n)
"""

def rob(nums: List[int]) -> int:
    dp = [-1] * len(nums)

    def dfs(i):
        nonlocal nums

        # base case: last house is reached or out of bounds
        if i >= len(nums):
            return 0
        if i == len(nums)-1:
            return nums[i]

        # just memoize from here 
        if dp[i] >= 0:
            return dp[i]
            
        # compare the max values of robbing or not robbing
        dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))
        return dp[i]

    return dfs(0)


# print(rob([2,9,8,3,6]))
# print(rob([1]))