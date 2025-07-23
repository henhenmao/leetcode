

from typing import List

"""
88. Merge Sorted Array (https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)
Follow up: Can you come up with an algorithm that runs in O(m + n) time?

idea:
keep a pointer at the last zero in nums1 that hasn't been updated
keep two pointers starting at the end of nums2 and the "end" of nums1
    let m be the number of elements (excluding end zeros) in the nums1 and n be the number of elements in nums2
    let i = m-1 and j = n-1
    since the two arrays are sorted, we know that max(nums1[i], nums2[j]) has to be the greatest value in the merged array
    do swaps to move the max value to the current zero and decrement the pointers for the zero and the array which had its value swapped

runtime: O(n + m)
space: O(1)
"""

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m-1
    j = n-1
    z = len(nums1)-1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[z] = nums1[i]
            i -= 1
        else:
            nums1[z] = nums2[j]
            j -= 1
        z -= 1
    
    while j >= 0:
        nums1[z] = nums2[j]
        j -= 1
        z -= 1


# nums1 = [4,0,0,0,0,0]
# nums2 = [1,2,3,5,6]
# merge(nums1, 1, nums2, 5)


