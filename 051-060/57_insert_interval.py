

from typing import List

"""
57. Insert Interval (https://leetcode.com/problems/insert-interval/description/?envType=problem-list-v2&envId=oizxjoit)
Note that you don't need to modify intervals in-place. You can make a new array and return it.

since you can easily do this question in O(n * log(n)) time probably should find a linear time algorithm 

initial intervals are sorted in ascending order and non-overlapping
find the two left and right intervals that potentially overlap with newInterval and merge them together if overlap

how to recognize an overlap:
    given two intervals i and j, we can compare the end of i with the start of j
    if the end of i is greater than the start of j, and the start of i is less than the end of j
        we can be sure that intervals i and j are overlapping

how to merge two intervals
    given intervals i and j:
    mergedInterval = [min(i[0], j[0]), max(i[1], j[1])]
    take the earliest start and the latest end of the two to get the merged interval

algorithm:
    1. iterate through intervals and add intervals to the result until an overlap is met
    2. once overlap is found, merge overlapping interals and update newInterval to the merged interval
    3. continue to iterate and merge overlaps until no more overlaps are found
    4. once no more overlaps exist, we know the rest of the intervals are normal (sorted and non overlapping)
    5. add the rest of the array to the result and return

runtime: O(n) where n is the number of intervals
space: O(n)

"""
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)
    res = []

    i = 0
    # keep going and adding intervals to res as long as no overlaps are observed
    while i < n and intervals[i][1] < newInterval[0]: # while the two selected intervals are not overlapping
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        curr = intervals[i]
        temp = [min(curr[0], newInterval[0]), max(curr[1], newInterval[1])]
        newInterval = temp
        i += 1
    
    res.append(newInterval)
    res = res + intervals[i:]
    return res


# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4, 8]
# insert(intervals, newInterval)



"""
you could just add the new interval to intervals, sort the array
and it's the exact same problem as 56. Merge Intervals (https://leetcode.com/problems/merge-intervals/description/)

runtime: O(n * log(n)) where n is the number of intervals
space: O(n) python sorting worst case space

"""

def insert2(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
    intervals.append(newInterval)
    intervals.sort()

    if len(intervals) <= 1:
        return intervals

    res = [intervals[0]]
    for curr in intervals[1:]:
        last = res[-1]

        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    return res

