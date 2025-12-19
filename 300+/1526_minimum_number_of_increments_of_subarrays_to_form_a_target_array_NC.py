

from typing import List

"""
1526. Minimum Number of Increments on Subarrays to Form a Target Array (https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/?envType=daily-question&envId=2025-10-30)


"""

def minNumberOperations(target: List[int]) -> int:
    res = 0
    prev = 0

    for curr in target:
        if curr > prev:
            res += curr - prev
        prev = curr
    return res

nums = [1,2,3,2,1]
print(minNumberOperations(nums))
            


    







