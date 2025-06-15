
from typing import List

"""
66. Plus One (https://leetcode.com/problems/plus-one/description/)

algorithm:
    1. start with a pointer at the rightmost digit (ones digit)
    2. add one to the current pointer digit
    3. if digit is a 9 and becomes 10, make it a 0 and have a carry for the next digit
    4. if the last digit in your loop is a 9, return the result with a 1 in front

runtime: O(n) where n is the number of digits
space: O(1)
"""
def plusOne(digits: List[int]) -> List[int]:
    carry = True
    i = len(digits)-1
    while i >= 0:
        if carry:
            digits[i] += 1
            carry = False

        if digits[i] == 10:
            digits[i] = 0
            carry = True
            if i == 0: # if last digit is a 9, make sure the carry is added and returned before the loop ends
                return [1] + digits
        i -= 1
    return digits