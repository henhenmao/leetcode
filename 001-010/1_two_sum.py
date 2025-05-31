
from typing import List

"""
1. Two Sum (https://leetcode.com/problems/two-sum/description/)

naive solution:
    use a double for loop to find all combinations of pairs that add up to target
    runtime of this algorithm is O(n^2) time, which is very slow.

more optimal solution:
    loop through all numbers in the list and hash the values and indexes into a hashmap
    use the value as a key and the index as value
    then perform another loop and for each number nums[i]:
        check if the dictionary contains target-nums[i]
        if the dictionary contains this value then you can be sure that
    this accomplishes the task in two passes O(n) time at the cost of O(n) space
"""

def twoSum(nums: List[int], target: int) -> List[int]:
    dict = {}
    for i in range(len(nums)):
        dict[nums[i]] = i
    for i in range(len(nums)):
        a = target-nums[i]
        if a in dict and dict[a] != i:
            return [i,dict[a]]
    return []

# print(twoSum([2,7,11,15], 9))