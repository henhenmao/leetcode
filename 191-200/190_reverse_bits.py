


"""
190. Reverse Bits (https://leetcode.com/problems/reverse-bits/?envType=problem-list-v2&envId=oizxjoit)
The input must be a binary string of length 32
Follow up: If this function is called many times, how would you optimize it?

- reverseBits(n) takes in n in integer form
- convert n into binary form with a 32 bit format and reverse the binary string
- convert the reversed binary string back into a base 10 integer

runtime: O(n) where n is the length of the binary string
space: O(n)
"""


def reverseBits(n: int) -> int: # n is binary input
    n = f"{n:032b}"[::-1] # converts the integer into a 32-bit binary string with leading zeros
    return (int(n, 2))