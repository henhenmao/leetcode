
from typing import List

"""
2016. Maximum Difference Between Increasing Elements (http://leetcode.com/problems/maximum-difference-between-increasing-elements/description/?envType=daily-question&envId=2025-06-16)

this is the exact same question as Best Time to Buy and Sell Stock (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
i don't think there's any difference between the two
nevermind there is a difference you need to return -1 if max profit is 0

algorithm:
    1. set the smallest price as prices[0], this will be the left side of the sliding window
    2. iterate through the prices, let p = the current price we are looking at in the loop
    3. if p is less than the smallest price, p is now the smallest price we have seen
        set smallest = p
    4. if p is greater than the smallest price, we check how much money we would make if we sold and compare it to our current maximum
    5. keep track of the current maximum

runtime: O(n) where n is the length of nums
space: O(1)
""" 

def maximumDifference(nums: List[int]) -> int:
    profit = 0

    smallest = nums[0]

    for n in nums:
        if smallest >= n:
            smallest = n
        else:
            temp = n - smallest
            profit = max(profit, temp)
    return profit if profit > 0 else -1
