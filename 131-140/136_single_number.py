
from typing import List

"""
136. Single Number (https://leetcode.com/problems/single-number/description/)
You must implement a solution with a linear runtime complexity and use only constant extra space.

this question is the coolest i've ever seen it amazes me because i'm not smart enough to understand it

XOR operator:
    xor (exclusive or) is an operator that takes two values and returns true (1) if the values differ and false (0) if they are the same
    ex. 0 ^ 0 = 0 (false)
        0 ^ 1 = 1 (true)
        1 ^ 1 = 0 (false)
        1 ^ 0 = 1 (true)

    you can also use bitwise XOR for integers
    ex. a = 5 -> 00000000000000000000000000000101
        b = 3 -> 00000000000000000000000000000011
        a ^ b -> 00000000000000000000000000000110

why does this matter:
    for this question, every number appears twice except for one
    notice how if we XOR the same number to itself, we always get 0
    ex. a = 5 -> 00000000000000000000000000000101
        b = 5 -> 00000000000000000000000000000101
        a ^ b -> 00000000000000000000000000000000

    also notice that if we XOR 0 and a number, we get the same number
    ex. a = 0 -> 00000000000000000000000000000000
        b = 5 -> 00000000000000000000000000000101
        a ^ b -> 00000000000000000000000000000101

    in this question, if we XOR every single number in nums, each element that appears twice will essentially cancel each other out
    since they have the same bits

    if every pair of numbers cancels out to 0, all that is left is the single number that only appears once

algorithm:
    1. start with res = 0
    2. use a loop to XOR every number in nums with res
    3. return res

runtime: O(n)
space: O(1)
"""


def singleNumber(nums: List[int]) -> int:
        # something to do with XOR since you can cancel out the bits or something
        res = 0
        for n in nums:
            res ^= n
        return res