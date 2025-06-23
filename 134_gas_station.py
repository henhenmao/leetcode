

from typing import List

"""
134. Gas Station (https://leetcode.com/problems/gas-station/description/)

i think if you just start at the gas station with the most gas and try from there
    if there is not enough gas to make a full circle then it is impossible
        might as well just start with the most gas if you're going to travel through everything anyways

ok maybe we can simplify the two arrays into one single array
    if we just calculate the gas profit of each gas[i] and cost[i]
        just do profit[i] = gas[i] - cost[i]
        positive profit means you gain gas after leaving gas station i
        negative profit means you lose gas after leaving gas station i

i'm thinking that after we create profits array of profit[i] = gas[i] - cost[i]
    we look for the maximum sum subarray to find the start index of the max sum subarray
    since the best index to start with is the one with the max sum
        since the gas stations are in a loop, we need to account for the maximum subarray wrapping around in the loop


don't actually need to make a profits array since if you can pointer i you can just calculate gas[i] - cost[i] at that moment

i got stuck and watched a neetcode tutorial for this problem
algorithm seems so easy now that i know it
i think what i was doing would have worked but had a lot of redundancies
still not sure how this deals with a subarray that loops around from end to start
    maybe it doesn't even matter

algorithm:
    1. iterate through both arrays and calculate the gas profits (gas[i]-cost[i])
    2. starting from i=0, build a subarray sum and keep track of the current sum of your subarray
    3. if your sum ever goes below 0, you ran out of gas and should just start over from where you are
    4. res will have the starting index of the max sum subarray


"""

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:

    if sum(gas) < sum(cost):
        return -1

    n = len(gas)

    curr = 0
    res = 0
    for i in range(n):
        curr += (gas[i]-cost[i])

        if curr < 0:
            curr = 0
            res = i+1
    return res




# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]

# gas = [4,2,3,4,5]
# cost = [0,4,5,6,2]

# print(canCompleteCircuit(gas, cost))