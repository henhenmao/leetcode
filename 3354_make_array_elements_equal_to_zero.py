
from typing import List

"""
3354. Make Array Elements Equal to Zero (https://leetcode.com/problems/make-array-elements-equal-to-zero/?envType=daily-question&envId=2025-10-28)

input constraints are very small so can just simulate the entire thing

from every 0 in nums, simulate it with both initial directions of left and right
    make sure you increment/decrement by 1 before the simulation happens so you can check out of bounds upon the first step

starting from index curr, repeat the following steps
1. check if curr is outside the range is nums
    if curr is outside range:
    check if every element in nums is 0, if true, return true, return false otherwise

2. check if nums[curr] == 0:
    if true, do not change your direction and just move along in your current direction
    increment curr by 1 if dir == True and decrement by 1 otherwise

3. if nums[curr] > 0:
    decrement the value of nums[curr] by 1
    change your direction, set dir = not dir
    increment curr by 1 if dir == True and decrement by 1 otherwise

runtime: O(n^2) where n is the length of nums
space: O(n) 
"""

def countValidSelections(nums: List[int]) -> int:

    n = len(nums)
    res = 0

    def simulation(nums, curr, dir):
        while 0 <= curr <= n-1:

            if nums[curr] == 0:
                curr += 1 if dir else -1
                continue

            nums[curr] -= 1
            dir = not dir
            curr += 1 if dir else -1

        if all(n == 0 for n in nums):
            return True
        return False
        
    for i in range(n):
        if nums[i] == 0:
            res += simulation(nums[:], i+1, True)
            res += simulation(nums[:], i-1, False)
            
    return res


nums = [1,0,2,0,3]
print(countValidSelections(nums))