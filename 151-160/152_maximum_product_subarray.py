
from typing import List

"""
152. Maximum Product Subarray (https://leetcode.com/problems/maximum-product-subarray/description/)

should be the same as the 53. Maximum Subarray (https://leetcode.com/problems/maximum-subarray/)
but with products instead of sums

assuming all positive elements in the array: returned value is the product of all nums
we need to consider just the possibilities of zeros and negative values.
    if zero: product = 0, reset
    if negative: anticipate a second negative value in the future
to anticipate for future negative values, we keep track of the current minimum product along with the current maximum product
    the minimum product is guaranteed to hold the most potential max product if there is a future negative value in the subarray

runtime: O(n)
space: O(1)
"""

def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    res = nums[0]
    currMax = nums[0]
    currMin = nums[0]

    for i in range(1, n):
        temp = max(nums[i], currMax * nums[i], currMin * nums[i]) # make sure currMin doesn't use updated currMax
        currMin = min(nums[i], currMax * nums[i], currMin * nums[i])
        currMax = temp
        res = max(res, currMax, currMin)

    return res