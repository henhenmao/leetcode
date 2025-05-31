
from typing import List


"""
56. Merge Intervals (https://leetcode.com/problems/merge-intervals/)

merging intervals:
    ex. [1,3] and [2,6]
        we know that these two intervals can be merged since the end of [1,3] comes after the start of [2,6]
        also notice that we can merge the two intervals into one interval than spans both
            take the start of the first interval and the end of the second interval
            [1,3] + [2,6] = [1,6]
    we can apply this rule iteratively to the entire list after sorting the list

algorithm:
    1. sort the intervals in ascending order
    2. compare the first two intervals and see if they can be merged
        if can be merged, merge them together
        if cannot be merged, move on to the next pair of intervals
    3. return the number of intervals in the list at the end

runtime: O(n * log(n)), where n is the length of intervals
    we did a linear iteration but we sorted
space: O(n)
"""


def merge(intervals: List[List[int]]) -> List[List[int]]:

    if len(intervals) <= 1:
        return intervals
    
    intervals.sort()
    res = [intervals[0]]

    for curr in intervals[1:]:
        last = res[-1]

        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    return res

print(merge([[1,4],[4,5]]))