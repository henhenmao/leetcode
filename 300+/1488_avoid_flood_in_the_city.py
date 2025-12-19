

from typing import List
import heapq
import bisect

"""
1488. Avoid Flood in The City (https://leetcode.com/problems/avoid-flood-in-the-city/description/?envType=daily-question&envId=2025-10-04)

you can dry a lake only when there is already water in it
    if you get multiple dry days at the start and no lakes have been filled, the dry days are pretty much useless
    
whenever you encounter a day with no rain (can dry a lake)
    add that day to a priority queue 

keep track of the last day that a lake was rained on
    if rain falls on a lake already filled, check two things
        1. the last day that the lake was rained on
        2. the earliest dry day that you have

    if the earliest dry day that you have takes place before the last day that the lake was rained on, discard that dry day and move onto the next earliest day
        if you run out of dry days, there will be a flood and you die 

algorithm:
    1. create hashmap lastRain where lastRain[i] is the last day the ith lake was rained on
        hashmap will contain pairs of (lake : last rain day)
    2. maintain a sorted array dryDays that will contain all days where you can possibly dry a lake
    3. create a list ans initially all set to -1
    4. iterate through the rains
        let lake = rains[i] = lake being rained on

        if rains[i] == 0, add the ith day to dryDays uisng bisect insort

        if rains[i] > 0, there is rain, so check if lastRain[i] != -1

            if lastRain does not contain lake as a key, the current lake has not been rained on so simply add a pair of lastRain[lake] to the current day (i)

            if rains[i] != -1, bisect right on dryDays to get the earliest dry day that occurs after lastRain[lake]
                if this day does not exist, flood happens and return empty array
                else: update the lastRain[lake] to be the current day
                    also update ans[dry day] to equal lake

runtime: O(n * logn) where n is the length of rains
space: O(n)     
"""


def avoidFlood(rains: List[int]) -> List[int]:

    n = len(rains)
    lastRain = {}
    dryDays = []
    ans = [1 for _ in range(n)]


    for i in range(n):
        lake = rains[i]

        if lake == 0:
            bisect.insort(dryDays, i)
            continue

        ans[i] = -1
        if lake not in lastRain:
            lastRain[lake] = i
            continue

        last = lastRain[lake]
        idx = bisect.bisect_right(dryDays, last)
        if idx == len(dryDays):
            return []
        dry = dryDays.pop(idx)
        ans[dry] = lake
        lastRain[lake] = i

    return ans


rains = [1,0,2,0,2,1]
print(avoidFlood(rains))

        
            


