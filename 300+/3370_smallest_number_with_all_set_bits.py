

"""
3370. Smallest Number with All Set Bits (https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-29)

numbers with all set bits are numbers that are 1 less than a power of two

1 = 2-1 = 1
3 = 4-1 = 11
7 = 8-1 = 111
15 = 16-1 = 1111

starting from m=2, check if m-1 >= n
    if true, return m
    else: multiply m by 2 to get to the next power of two

    continue this loop forever but i put an upper bound of 2048 since the constraints make n <= 1000
        so the highest value of m that can be returned is 1028

runtime: O(1)
space: O(1)
"""

def smallestNumber(n: int) -> int:
    m = 2
    while m < 2048:
        if m-1 >= n:
            return m-1
        m = m << 1