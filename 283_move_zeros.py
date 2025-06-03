

from typing import List

"""
283. Move Zeros (https://leetcode.com/problems/move-zeroes/description/)
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Follow up: Could you minimize the total number of operations done?

wait can you just remove all zeros and just push them to the end
idk if this is the optimal solution
i'm not improving on this

runtime: O(n^2) where n is the length of nums
space: O(1)


"""

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    i = 0
    count = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            count += 1
        else:
            i += 1

    for _ in range(count):
        nums.append(0)
