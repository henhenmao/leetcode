
from typing import List

"""
2110. Number of Smooth Descent Periods of a Stock (https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/?envType=daily-question&envId=2025-12-15)

- a single day is a considered a smooth descent period
- a smooth descent period ex. (4, 3, 2, 1) contains more smooth descent periods
    - for any smooth descent period, the total number of smooth descent periods contained is k(k+1)/2 where k is the size of the period

- find the largest possible subarray of contiguous days such that the price of each day is lower than the preceding day by 1
    - count the size of that subarray -> there are k(k+1)/2 smooth descent periods

ex. prices = [3,2,1,4]

[3,2,1] is the first subarray we find (adding 4 to the subarray will break the pattern)
k = 3
3(3+1)/2 = 6 -> there are 6 smooth descent periods inside of this subarray -> add 6 to the total

[4] is the next subarray we find (before reaching the end of the list)
k = 1
1(1+1)/2 = 1 -> single smooth descent period -> add 1 to the total

algorithm:
    1. set prev to price[0]+1 as to allow the first element to be the first element of a smooth descent period
    2. start from the first element, count the number of elements until prices[i-1] - prices[i] != 1, count this in currPeriod
        - update prev to the current element at the end of each iteration
    3. once the pattern breaks, add currPeriod*(currPeriod+1)//2 to the total (number of smooth descent periods within the large one we just saw)
        - reset currPeriod to 1 when the pattern break
    4. add currPeriod*(currPeriod+1)//2 once more at the very end cause the very end isn't counted in the loop

runtime: O(n) where n is the length of prices
space: O(1)
"""

def getDescentPeriods(prices: List[int]) -> int:
    n = len(prices)

    if n == 0:
        return 0

    res = 0
    currPeriod = 0
    prev = prices[0]+1
    for curr in prices:
        if prev-curr == 1:
            currPeriod += 1
            prev = curr
            continue
        else:
            res += currPeriod * (currPeriod+1) // 2
            currPeriod = 1
            prev = curr
        
    res += currPeriod * (currPeriod+1) // 2
    return res


prices = [3,4,3]
print(getDescentPeriods(prices))

