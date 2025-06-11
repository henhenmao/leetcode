

from typing import List

"""
33. Search in Rotated Sorted Array (https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=oizxjoit)
You must write an algorithm with O(log n) runtime complexity.

nums is sorted in ascending order with distinct values and is possibly rotated at a pivot
binary search question since we are looking for an element in a "sorted" array in log n time

[0,1,2,4,5,6,7] with pivot 3 -> [4,5,6,7,0,1,2]

we should find the pivot using binary search aka where two adjacent elements are in descending order
    we may be able to do this by finding the minimum element
once the pivot point is found, we pretty much have two separate sorted arrays
we can just determine which sorted array the target value is in and perform a binary search on the right one as usual


algorithm:
    1. find the index of the minimum value of the sorted rotated array
        the minimum value splits the array into two separate sorted lists you can perform a binary search on
    2. determine which of the two sorted lists you want to set your binary search pointers to
        let pivot = the index of the minimum value of the sorted array
        if target in the left of the pivot, set low = 0 and high = pivot-1
        if to in the right of the pivot, set low = pivot and high = len(nums)-1
        if the minimum value is at index 0, the array is not rotated and you can just set low = 0 and high = len(nums)-1
    3. do a standard binary search wiht your new pointers and find the target and return -1 if not found

runtime: O(log(n)) two binary searches are performed
space: O(1)
"""

def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low + high)//2
        
        # if mid is greater than high (upper half is not sorted), check the upper half
        # if mid is less than high (uppper half is sorted), check the lower half
        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid+1

    # mid now is the index of the minimum value
    # the second sorted array begins at index mid
    # if mid == 0 then there is no pivot rotation

    # determine where to put the two new pointers

    if mid == 0:
        low = 0
        high = len(nums)-1
    else:
        if target >= nums[0] and target <= nums[mid-1]:
            low = 0
            high = mid-1
        elif target >= nums[mid] and target <= nums[-1]: # target is in the second sorted array
            low = mid
            high = len(nums)-1
    
    # standard binary search i think
    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            low = mid+1
        else:
            high = mid-1

    return -1


# nums = [4,5,6,7,8,9]
# target = 8
# print(search(nums, target))