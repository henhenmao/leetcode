
from typing import List

"""
217. Contains Duplicate

sets make this question very easy

sets cannot contain duplicates
    if a list is converted to a set, all duplicates are removed

algorithm:
    1. create a set out of nums
    2. compare the lengths of the original list and the set of nums
    3. if the lengths are different, then we know that a duplicate was removed, and that a duplicate exists in nums
    4. if the lenghts are the same, then there were no duplicates removed, and that there were no duplicates

runtime: O(n)
space: O(n)
"""


def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))