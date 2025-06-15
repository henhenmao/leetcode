
from typing import List

"""
2032. Two Out of Three (https://leetcode.com/problems/two-out-of-three/description/)

we can just use set theory to find values present in at least two of the three arrays

algorithm:
    1. convert all three arrays into sets
    2. get the intersection between (nums1 and nums2), (nums2 and nums3), and (nums3 and nums1)
    3. union all three intersection sets
    4. convert final set into a list and return

runtime: O(n) where n is the length of each array assuming they are all the same length
space: O(n)
"""

def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        return list(((nums1.intersection(nums2)).union(nums2.intersection(nums3))).union(nums1.intersection(nums3)))