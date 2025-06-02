
from typing import List

"""
40. Combination Sum II (https://leetcode.com/problems/combination-sum-ii/description/)

we pretty much want to do the same thing as the last question
the only difference is that there are duplicates in the candidates pool and we cannot have duplicates in the result
    we can fix this problem by sorting the candidates and skipping adjacent duplicates when choosing candidates
    since each different duplicate can be used once, we only skip adjacent duplicates within the same for loop

algorithm:
    1. sort candidates so that the duplicates are adjacent to each other
    2. loop through each number in nums starting at index i (nums[j])
    3. add nums[j] to the current path and current sum
    4. recurse with updated current path and total sum
        use j again in the recursion to allow reuse of the same number but not previous numbers
    5. after recursion, pop element from the current path to backtrack and try next number
    6. if the next number is a duplicate then skip and so on for multiple duplicates

runtime: O(2^n) where n is the number of candidates, O(n(log(n))) + O(2^n)???
space: O(n)
"""

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def dfs(curr, total, i):
        # base case
        if total >= target:
            if total == target:
                res.append(curr[:])
            return
            
        for j in range(i, len(candidates)):
            # skip any duplicates in the same loop
            if j > i and candidates[j] == skip:
                continue

            curr.append(candidates[j])
            dfs(curr, total+candidates[j], j+1)
            skip = curr.pop()
        return
    dfs([], 0, 0)
    return res