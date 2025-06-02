
from typing import List

"""
39. Combination Sum (https://leetcode.com/problems/combination-sum/description/)

keep adding every element in a loop and branch out with dfs for each element
if current total exceeds the target then backtrack
if current total equals the target then add to the result

algorithm:
    1. loop through each number in nums starting at index i (nums[j])
    2. add nums[j] to the current path and current sum
    3. recurse with updated current path and total sum
        use j again in the recursion to allow reuse of the same number but not previous numbers
    4. after recursion, pop element from the current path to backtrack and try next number

runtime: O(2^n) - where n is the length of nums???
space: O(t) - since the longest sum is 1+1+1+1.... t times ???
"""

def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(curr, total, i):
        nonlocal res

        # base case: total exceeds or equals target
        # add to result if equal
        if total >= target:
            if total == target:
                res.append(curr[:]) # be sure to create a shallow copy of curr before adding to res
            return
        
        for j in range(i, len(nums)):
            curr.append(nums[j])
            dfs(curr, total+nums[j], j)
            curr.pop()
        return
    
    dfs([], 0, 0)
    return res