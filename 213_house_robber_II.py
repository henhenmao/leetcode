
from typing import List

"""
213. House Robber II (https://leetcode.com/problems/house-robber-ii/description/)

ok why can't i just do the same thing as the first house robber question 
    since the only difference between this question and the original house robber question is the adjacency of the first house and the last house,
        we can just run the house robber algorithm twice
        1. we can find the maximum money you can rob when you exclude the first house (second house to last house)
        2. we can also find the maximum money you can rob when you exclude the last house (first house to second-last house)
        after getting both values we can just return the higher amount

runtime: O(n) where n is the number of houses
space: O(n)

"""

def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    dp1 = [-1] * len(nums) # two dp arrays for two different dfs 
    dp2 = [-1] * len(nums)

    def dfs(i, curr_dp):
        # base case: last house is reached or out of bounds
        if i >= len(nums):
            return 0
                
        if i == len(nums)-1:
            return nums[i]

        # just memoize from here 
        if curr_dp[i] >= 0:
            return curr_dp[i]
            
        # compare the max values of robbing or not robbing
        curr_dp[i] = max(nums[i] + dfs(i+2, curr_dp), dfs(i+1, curr_dp))
        return curr_dp[i]

    # start first dfs at the second house 
    second_to_last = dfs(1, dp1)
    nums.pop() # removing the last house for the seocnd dfs
    first_to_second_last = dfs(0, dp2)
    return max(first_to_second_last, second_to_last)

# print(rob([2,9,8,3,6]))