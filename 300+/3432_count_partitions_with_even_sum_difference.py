
from typing import List

"""
3432. Count Partitions with Even Sum Difference (https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/?envType=daily-question&envId=2025-12-05)

let a = sum of left partition, b = sum of right partition, and c = total sum of nums

left = a
right = c-a

difference = right-left
= b-a
= (c-a)-a
= c-2a

algorithm:
    1. get the total sum of nums
    2. iterate through nums 
    3. keep track of a = sum so far from the left side
    4. if c-2a is even, add to result
    5. return result

runtime: O(n) where n is the length of nums
space: O(1)
"""

def countPartitions(nums: List[int]) -> int:

    res = 0
    c = sum(nums)

    soFar = 0
    for i in range(len(nums)-1):
        a += nums[i]
        if (c-2*a)%2 == 0:
            res += 1

    return res