
from typing import List

"""
4. Median of Two Sorted Arrays (https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

i did NOT solve this in the intended way but i'm just going to put this here
what's really funny is that when i first started out i thought i was so smart for doing this in a few lines

i bet the real solution is crazy difficult
"""


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        new_list = sorted(nums1 + nums2)
        if len(new_list) % 2 == 1:
            return new_list[len(new_list)//2]
        return (new_list[len(new_list)//2] + new_list[len(new_list)//2-1])/2