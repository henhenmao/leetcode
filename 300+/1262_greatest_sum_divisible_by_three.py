

from typing import List

"""
1262. Greatest Sum Divisible by Three (https://leetcode.com/problems/greatest-sum-divisible-by-three/description/?envType=daily-question&envId=2025-12-01)

we want to make as many groups of numbers that form a multiple of three
all ways many (or one) numbers can make a multiple of 3
1. all multiples of three go into total
2. if (n%3 == 1) and (m%3 == 2, the two numbers form a multiple of 3
3. if (n%3 == m%3 == k%3), the three numbers form a multiple of 3

i think out of options 2 and 3, you should always greedily choose the one that gives the greatest sum

wait wait wait im stupid ahhh

what if we just excluded a few or one elements from the total sum instead of building the sum ourselves
let currentMod = the amount of remainder we need to exclude for the sum to be divisible by 3
if currentMod == 1, compare taking the smallest mod1 element to taking the smallest two mod2 elements
if currentMod == 2, compare taking the smallest mod2 element to taking the smallest two mod1 elements
out of the two options at each scenario, choose the minimum amount as to maximize the sum

runtime: O(log(n)) where n is the length of nums
space: O(n)
"""

def maxSumDivThree(nums: List[int]) -> int:

    mod1 = []
    mod2 = []

    total = sum(nums)
    currentMod = total%3

    if currentMod == 0:
        return total

    res = total

    for n in nums:
        if n % 3 == 1:
            mod1.append(n)
        elif n % 3 == 2:
            mod2.append(n)

    mod1.sort(reverse=True)
    mod2.sort(reverse=True)

    smallestmod1 = total+1
    smallestmod2 = total+1

    if currentMod == 1:
        if mod1:
            smallestmod1 = mod1[-1]
        if len(mod2) >= 2:
            smallestmod2 = mod2[-1] + mod2[-2]

        if smallestmod1 < smallestmod2:
            res -= mod1.pop()
        else:
            res -= smallestmod2
            mod2.pop()
            mod2.pop()

    elif currentMod == 2:
        if mod2:
            smallestmod2 = mod2[-1]
        if len(mod1) >= 2:
            smallestmod1 = mod1[-1] + mod1[-2]

        if smallestmod2 < smallestmod1:
            res -= mod2.pop()
        else:
            res -= smallestmod1
            mod1.pop()
            mod1.pop()

    return res

nums = [2,19,6,16,5,10,7,4,11,6]
print(maxSumDivThree(nums))