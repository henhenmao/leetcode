

from typing import List

"""
33. Search in Rotated Sorted Array (https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=problem-list-v2&envId=oizxjoit)
You must write an algorithm with O(log n) runtime complexity.

nums is sorted in ascending order with distinct values and is possibly rotated at a pivot
binary search question since we are looking for an element in a "sorted" array in log n time

[0,1,2,4,5,6,7] with pivot 3 -> [4,5,6,7,0,1,2]

we should find the pivot using binary search aka where two adjacent elements are in descending order


"""


def search(nums: List[int], target: int) -> int:
    pass