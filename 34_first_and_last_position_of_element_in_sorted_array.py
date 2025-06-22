

from typing import List

"""
34. Find First and Last Position of Element in Sorted Array (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/)

to get the first position of target element, we need to find index i, where nums[i] == target and nums[i-1] < target
    or nums[i] == target and i == 0 (first element in nums)
to get the last position of target element, we need to find index j, where nums[j] == target and nums[j+1] > target
    or nums[j] == target and j == len(nums)-1 (last element in nums)

do two sepeate binary searches to find indexes i and j

runtime: O(log(n)) where n is the length of nums
space: O(1)

"""

def searchRange(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    i, j = -1, -1

    # first binary search for index i
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high)//2

        if nums[mid] == target:
            if mid == 0:
                i = mid
                break
            if nums[mid-1] != nums[mid]:
                i = mid
                break
            high = mid-1
        
        elif nums[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1

    # second binary search for j
    low = 0
    high = n-1
    
    while low <= high:
        mid = (low + high)//2

        if nums[mid] == target:
            if mid == n-1:
                j = mid
                break
            if nums[mid+1] != nums[mid]:
                j = mid
                break
            low = mid+1
        
        elif nums[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return [i, j]


# nums = [2,2]
# target = 2
# print(searchRange(nums,target))



