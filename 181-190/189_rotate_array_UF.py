
from typing import List

"""
189. Rotate Array (https://leetcode.com/problems/rotate-array/description/)
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

algorithm:
    1. take the mod of k and len(nums) since rotating the array len(nums) times gives the same array
    2. reverse nums
    3. reverse the sublist up to k
    4. reverse the sublist from k to the end

ex. nums = [1,2,3,4,5,6,7], k = 3
    1. k = 3
    2. nums = [7,6,5,4,3,2,1]
    3. nums = [5,6,7,4,3,2,1]
    4. nums = [5,6,7,1,2,3,4]

runtime: O(n)
space: O(n) - can be improved

"""

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    k %= len(nums)
    nums.reverse()

    nums[k:] = reversed(nums[k:])
    nums[:k] = reversed(nums[:k])