

from typing import List

"""
77. Combinations (https://leetcode.com/problems/combinations/description/)

this is a standard backtracking problem where you get every combination using dfs or something

algorithm:
    1. use dfs to get every build every combination from numbers of 1 to n
    2. backtrack when your sublist becomes longer than k or you reach the end
    3. add all combinations of size k into the result

runtime: O(C(n, k) * k), C(n, k) are the number of total combinations of n choose k
    we multiply C(n * k) by k since for every combination, we make a copy of the built subarray of size k to the result
space: O(C(n, k) * k)
"""


def combine(n: int, k: int) -> List[List[int]]:
    res = []

    def dfs(i, curr):   
        nonlocal res

        if len(curr) == k:
            res.append(curr[:])
            return

        if i > n:
            return

        for j in range(i, n+1):
            curr.append(j)
            dfs(j+1, curr)
            curr.pop()

    dfs(1, [])
    return res



n = 4
k = 2
print(combine(n, k))
