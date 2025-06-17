
from typing import List

"""
121. Best Time to Buy and Sell Stock (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

use a sliding window to keep track of the smallest price we come across and the largest price we come across given the current smallest price
we keep sliding through the prices and think of these two things:
    1. what is the lowest price we have seen so far
    2. what is the maximum profit we can get if we sell today from the lowest price

algorithm:
    1. set the smallest price as prices[0], this will be the left side of the sliding window
    2. iterate through the prices, let p = the current price we are looking at in the loop
    3. if p is less than the smallest price, p is now the smallest price we have seen
        set smallest = p
    4. if p is greater than the smallest price, we check how much money we would make if we sold and compare it to our current maximum
    5. keep track of the current maximum

runtime: O(n) where n is the number of prices
space: O(1)
"""

def maxProfit(prices: List[int]) -> int:
    profit = 0

    smallest = prices[0]
    for p in prices:
        if smallest >= p:
            smallest = p
        elif p > smallest:
            temp = p - smallest
            profit = max(temp, profit)
    return profit