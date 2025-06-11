
from typing import List

"""
322. Coin Change (https://leetcode.com/problems/coin-change/?envType=problem-list-v2&envId=oizxjoit)

elite ball knowledge required for this question
    coin change is a dynamic programming question pretending to be a greedy problem
    initial intuition is to just keep adding the greatest coin you can add to reach the amount
    this greedy algorithm does not work for cases like
        coins = [1,3,4], amount = 6
        greedy algorithm will do 6 - 4 - 1 - 1 = 3 coins
        actual answer would be 6 - 3 - 3 = 2 coins

    i dont wanna do this rn

"""

 
def coinChange(coins: List[int], amount: int) -> int:
    pass