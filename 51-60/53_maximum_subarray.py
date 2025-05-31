
from typing import List

"""
53. Maximum Subarray (https://leetcode.com/problems/maximum-subarray/)

kadane's algorithm:
    find the maximum possible sum for each subarray ending at nums[i] have a maximum sum variable
    and adding nums[i] to the current sum if current sum + nums[i] is ever less than nums[i], you
    start over your sum starting at nums[i]
    (because starting from nums[i] is better than including the previous sum and nums[i])

runtime: O(n) only traverses the array once
space: O(1)

"""


def maxSubArray(nums: List[int]) -> int:

        curr = nums[0]
        res = nums[0]

        for n in nums[1:]:
            curr = max(n, n + curr)
            res = max(res, curr)
        
        return res