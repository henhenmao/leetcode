
from typing import List


"""
14. Longest Common Prefix (https://leetcode.com/problems/longest-common-prefix/description/)

algorithm:
    1. sort the array lexicographically
    2. compare the first and last word in the sorted array
    3. find the longest common prefix between the the first and last element in the array
    4. just keep iterating and stop when they don't match
we can do this because since we sorted the array of strings, anything common between the first and last
must also be common for all strings in between them

runtime: O(n * log(n)), where n is the length of strs
space: O(n) maybe - i don't actually know if sorting uses constant space or not

"""


def longestCommonPrefix(strs: List[str]) -> str:
    strs.sort()
    prefix = ""
    shortest = strs[0]
    longest = strs[-1]
    for i in range(len(shortest)):
        if shortest[i] != longest[i]:
            return prefix
        prefix += shortest[i]
    return prefix