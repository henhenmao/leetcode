
from typing import List

"""
35. Search Index Position (https://leetcode.com/problems/search-insert-position/)
You must write an algorithm with O(log n) runtime complexity.

naive solution at the bottom:
    look for the target in nums with a loop
    if the target is not found:
        go through nums again and find the right index

just do a binary search lol
thats the entire question

algorithm: 
    1. set low and high pointer
    2. set mid pointer between low and high
    3. check where target is relative to the middle
        if nums[mid] == target: you found the index
        if nums[mid] < target: the target is in the upper half of your mid pointer -> increase your low pointer to mid
        if nums[mid] > target: the target is in the lower half of your mid pointer -> decrease your high pointer to mid
    4. if target is never found, your low pointer will end up at the index it should be in the end

runtime: O(log(n))
space: O(1)
"""

def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] < target: # target is in upper region
            low = mid + 1
        
        if nums[mid] > target: # target is in lower region
            high = mid - 1
    return low




"""
naive solution from a few months ago
what are you doing

runtime: O(n)
space: O(1)
"""

def searchInsert(nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target in nums:
            return nums.index(target)
        for i in range(len(nums)-1):
            if target > nums[i] and target < nums[i+1]:
                return i+1


