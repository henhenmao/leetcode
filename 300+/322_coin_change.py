
from typing import List
from collections import deque

"""
322. Coin Change (https://leetcode.com/problems/coin-change/?envType=problem-list-v2&envId=oizxjoit)

elite ball knowledge required for this question
    initial intuition is to just keep adding the greatest coin you can add to reach the amount
    this greedy algorithm does not work for cases like
        coins = [1,3,4], amount = 6
        greedy algorithm will do 6 - 4 - 1 - 1 = 3 coins
        actual answer would be 6 - 3 - 3 = 2 coins

    hahhahaha im so smart for knowing this bahahahhahaha
        
    i dont wanna do this rn

ok i'm back like a few weeks later lmao

just gonna do the following:
    1. sort the coins in descending order (1 <= coins.length <= 12) so not a big deal
    2. do a dfs that tries different coin combinations with backtracking
    3. use a dp table to reduce redundant coin combinations
        dp table will contain the minimum coin amount for dp[coin amount]

runtime: O(n * k) where n is the number of coins and k is the amount
    this is because for each value of total from 0 to k, we are finding a combination of n coins
space: O(k) dp array
"""

def coinChange(coins: List[int], amount: int) -> int:
    n = len(coins)
    coins.sort(reverse=True)

    dp = [20000] * (amount+1)

    res = amount+1    
    def dfs(i, total, coinCount):
        nonlocal res

        # base cases where we can backtrack
        if i == n or total > amount or coinCount >= res:
            return

        # update the minimum coin count when a combination of coins is found
        if total == amount:
            res = min(res, coinCount)
            return
        
        # using a dp table to ignore paths that lead to a worse coinCount
        if dp[total] <= coinCount:
            return
        
        dp[total] = coinCount
        
        # trying combinations of coins
        for j in range(i, n):
            dfs(j, total+coins[j], coinCount+1)
    
    dfs(0, 0, 0)
    return res if res != amount+1 else -1

# coins = [3,7,405,436]
# amount = 8839
# print(coinChange(coins, amount))