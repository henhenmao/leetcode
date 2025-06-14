

"""
191. Number of 1 Bits (https://leetcode.com/problems/number-of-1-bits/?envType=problem-list-v2&envId=oizxjoit)
Follow up: If this function is called many times, how would you optimize it?

getting number of 1s in the bits:
    we can tell whether or not the rightmost bit is a 1 or not by doing a modulo operation
    ex. 9 % 2 (0b1001 % 2) = 1
        8 % 2 (0b1000 % 2) = 0
    after determine the state of the rightmost bit of the binary representation, we can all of the other bits to the right by one
        so that the tens place bit becomes the new rightmost bit
        idk where the original ones place bit goes

runtime: O(1) since length of the binary string is maximum 32 so O(32) = O(1)
space: O(1)
"""

def hammingWeight(n: int) -> int:
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res