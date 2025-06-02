
from typing import List


"""
746. Min Cost Climbing Stairs (https://leetcode.com/problems/min-cost-climbing-stairs/description/)

just do the same thing as the first climbing stairs
but keep track of all the costs of each stair so far
use a memo table to store the minimum cost from each step n

algorithm:
    1. starting at the first step, there are two possibilities: step up 1 or step up 2
    2. recurse into these two possibilities 
    3. set the minimum cost from step n to cost[n] + min(dfs(n+1), dfs(n+2))
        memoize this value into the dp table since a lot of the recursion is repeated

runtime: O(n)
space: O(n)
"""


def minCostClimbingStairs(cost: List[int]) -> int:

    dp = [-1] * 1005

    def dfs(n):
        nonlocal dp
        if dp[n] != -1:
            return dp[n]
        if n >= len(cost):
            return 0
        dp[n] = cost[n] + min(dfs(n+1), dfs(n+2))
        return dp[n]

    return min(dfs(0), dfs(1))