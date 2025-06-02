
from typing import List


"""
216. Combination Sum III (https://leetcode.com/problems/combination-sum-iii/)

we can use a dfs algorithm + backtracking to get all possibilities of digits

for each digit: we can either add it or not add it
    once we encounter a digit, we never look at it ever again for that dfs branch
        we only want to use a digit at most one time
    if we ignore a digit, we don't want to encounter it again
        since it may create duplicate combinations with other dfs branches where that digit was added

algorithm:
    1. get as many combinations of digits you can with dfs backtracking
        keep track of the current sum of numbers you have
        also keep track of which numbers you have already encountered
        keep track of the current subset of digits you have
    2. base cases:
        if your sum overshoots the target value: backtrack
        if your sum equals the target value: add your subset to the final result

runtime: O(9^n) you have a max of 9 possibilities for n dfs iterations
space: O(9^n)
"""


def combinationSum3(k: int, n: int) -> List[List[int]]:
    res = []
    def combinations(i, k, total, curr):
        if k == 0:
            if total == n:
                res.append(curr[:])
            return
        if total > n:
            return

        for j in range(i+1, 10):
            curr.append(j)
            combinations(j, k-1, total+j, curr)
            curr.pop()
    combinations(0, k, 0, [])
    return res

# print(combinationSum3(3, 7))