

from typing import List

"""
1437. Check If All 1's Are at Least Length K Places Away (https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/?envType=daily-question&envId=2025-11-17)

find the index of the first 1 value
from that index, count increments until the next 1 is encountered
if less steps are taken than k when a new 1 is found, that means there is a gap that is not at least length k between 1's, return false

if the end of the list is reached, all gaps are valid, return true

runtime: O(n) where n is the length of nums
space: O(1)
"""

def kLengthApart(nums: List[int], k: int) -> bool:
    n = len(nums)
    i = 0

    # getting the index of the first 1
    while i < n:
        if nums[i]:
            break
        i += 1

    places = 0
    i += 1

    # counting gaps between each 1 value, reseting the count when a new 1 is encoutered
    while i < n:
        if not nums[i]:
            i += 1
            places += 1
            continue

        if places < k:
            return False
        
        places = 0
        i += 1
    
    return True


nums = [1,0,0,0,1,0,0,1]
print(kLengthApart(nums, 2))