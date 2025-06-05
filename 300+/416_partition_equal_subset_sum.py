
from typing import List

"""
416. Partition Equal Subset Sum (https://leetcode.com/problems/partition-equal-subset-sum/description/)

we only need to keep track of one partition, since we can just subtract sum(first partition) from sum(nums) to get sum(second partition)
we need to get every partition of nums

actually we don't even need to keep track of partitions
our target is to achieve a subset with the sum of sum(nums)//2
so we just need to keep track of our current count
this is the subset sum problem https://en.wikipedia.org/wiki/Subset_sum_problem

this question actually cooked me bad

dp: dp[j] means that a subset sum of j is possible with the current set of numbers
    dp[0] is True at the start since a subset sum of 0 is always possible (empty subset)

algorithm:
    1. case: if sum of all numbers is odd, return False immediately
    2. set target as sum(nums)//2: sum we are trying to build in the subset
    3. set dp table
    4. for each number num in nums, update dp[j] from target down to nums
        we iterate in reverse order to avoid overwriting values involved in future updates
    5. if dp[j-num] is reachable, then so is j (if we add num)
    6. see if dp[target] is among the numbers that can be reached

runtime: O(n * sum(nums)//2)
space: O(sum(nums)//2)
    
"""


def canPartition(nums: List[int]) -> bool:
    total = sum(nums)

    if total % 2 == 1:
        return False

    target = total//2

    dp = [False] * (target+1)
    dp[0] = True # a zero sum is always possible

    for num in nums:
        for j in range(target, num-1, -1):
            dp[j] = dp[j] or dp[j-num]

    return dp[target]



# nums = [99, 97, 100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,98,100]
# nums = [1,5,11,5]
# print(canPartition(nums))