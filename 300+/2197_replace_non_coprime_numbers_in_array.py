

import math
from typing import List
from collections import deque

"""
2197. Replace Non-Coprime Numbers in Array (https://leetcode.com/problems/replace-non-coprime-numbers-in-array/description/?envType=daily-question&envId=2025-09-16)

1. find any two adjacent numbers in nums that are non-coprime
    non-coprime means that the two numbers have at least one common factor
2. if no such pairs of numbers exists, stop
3. otherwise, delete the two numbers and replace them with their LCM
    LCM is the least common multiple
4. continue this process as as long as two adjacent non-coprime pairs in nums exists
5. return the final array after modifications to nums

how to know if two numbers are coprime
    Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.
    we can use python math.gcd function to check if two numbers are coprime or not

how to get the LCM of two numbers 
    thankfully python has a math.lcm function as well


actual algorithm:
    1. iterate through nums while looking at pairs of adjacent numbers
    2. for every pair of numbers, check if they are coprime by using python gcd
        if gcd(nums[i], nums[i+1]) == 1, the two adjacent numbers are coprime
        otherwise, they are non-coprime
    3. for each number, compare that current number to the top of the stack, these two numbers are adjacent
    4. if two adjacent numbers are found to be coprime, add the current value to the stack
    5. if two adjacent numbers are found to be non-coprime, merge them together into an LCM and add that to the stack
        check the top of the stack, the most recent value we have seen or created so far, if the current merge can be merged with the top of the stack
        recursively check the top of the stack and merge current value with the top of the stack until the top of the stack and the current value are coprime
    6. in the end, the final stack should contain the final list to be returned

    
runtime: O(n * log(k)) where n is the length of nums and k is the greatest number in nums
space: O(n)
"""

def replaceNonCoprimes(nums: List[int]) -> List[int]:
    def recallmerge(curr):
        if not stack:
            stack.append(curr)
            return
        
        prev = stack.pop()
        if math.gcd(curr, prev) == 1:
            stack.append(prev)
            stack.append(curr)
            return
        
        recallmerge(math.lcm(curr, prev))


    if len(nums) <= 1:
        return nums

    stack = []

    for i in range(len(nums)):
        curr = nums[i]

        # edge case where the stack is empty
        if not stack:
            stack.append(curr)
            continue

        prev = stack[-1]
        
        # if the pair is coprime: add both back to the stack and continue
        if math.gcd(curr, prev) == 1:
            stack.append(curr)

        # if the current pair is non-coprime, merge the two numbers into the LCM
        else:
            stack.pop()
            lcm = math.lcm(curr, prev)
            stack.append(lcm)

            # recursively check the previous 
            recallmerge(lcm)

    return stack


nums = [2,2,1,1,3,3,3]
print(replaceNonCoprimes(nums))
