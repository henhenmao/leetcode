 
from typing import List

"""
55. Jump Game (https://leetcode.com/problems/jump-game/description/)

for this question, you simply just need to keep track of the furthest index you can travel to
i remember this analogy i saw online:
    imagine you are a car driving in a straight line and each index is a gas station that fill different amounts of gas
    now that i think about it the analogy sucks why wouldn't i just fill my gas at every stop
    i guess you can only fill your gas if you have less than what is offered
    i think i'm remembering it wrong

algortihm:
    1. set the current furthest you can travel to the nums[0] (since you start there)
    2. max_index is essentially your "fuel", so whenever you increment i you check if you used more fuel than you have
    3. at every index, check if you can go further with the fuel at that index
    4. if you make it to the end return true

runtime: O(n) one single pass
space: O(1)
"""


def canJump(nums: List[int]) -> bool:    
    n = len(nums)

    if n == 1:
        return True

    max_index = nums[0]
    i = 1
    while i <= max_index:

        temp = i + nums[i]
        max_index = max(temp, max_index)

        if max_index >= n-1 or i == n-1:
            return True
        i += 1
    return False
