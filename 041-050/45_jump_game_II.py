
from typing import List

"""
45. Jump Game (https://leetcode.com/problems/jump-game-ii/description/)

when at nums[i], we need to do the following:
    - traverse the areas that can be jumped to (will call an area nums[j])
    - calculate which of those areas lead to the furthest distance (j + nums[j])
    - jump to that area and repeat

algorithm:
    1. starting at i = 0, traverse areas that can be jumped from nums[i]
        traverse from i+1 to i + nums[i] + 1
    2. find the maximum distance that can be covered from an area and jump to that area
    3. count the numbe of jumps taken the entire way through
    4. if the end can be reached from a jump, jump to the end and return the number of jumps

runtime: O(n) each element is traversed once
space: O(1)
"""


def jump(nums: List[int]) -> int:
    jumps = 0
    i = 0
    if len(nums) == 1:
        return 0

    while True:
        n = nums[i]
        temp_max = i
        next_index = nums[i]

        if i + n >= len(nums)-1:
            return jumps + 1

        for j, temp_val in enumerate(nums[i+1: i+n+1]):
            temp = i + j + 1 + temp_val
            if temp > temp_max:
                temp_max = temp
                next_index = i + j + 1
    
        jumps += 1
        i = next_index