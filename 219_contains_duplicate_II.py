

from typing import List

"""
219. Contains Duplicate II (https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150)

create a set to check for duplicate values
    maintain a sliding window of size k+1 inside of the set
    if we try to add a value inside of this sliding window set and the value already exists:
        we know that there is a duplicate and that duplicate is within k of each other
    
    iterate over nums with i and add nums[i] to the set at each iteration
    when the sliding window is full, shrink the left end of the window by removing nums[i-k] from the set

runtime: O(n)
space: O(n)
"""

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    window = set()

    for i in range(len(nums)):
        if nums[i] in window:
            return True
        
        window.add(nums[i])

        if len(window) > k:
            window.remove(nums[i - k])
        
    return False

nums = [99,99]
k = 2
print(containsNearbyDuplicate(nums, k))




