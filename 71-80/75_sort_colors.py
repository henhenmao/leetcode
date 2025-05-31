
from typing import List

"""
75. Sort Colors (https://leetcode.com/problems/sort-colors/)

this question absolutely cooked me i had to look at the solution
this is a problem called the dutch national flag problem (https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/)

dutch national flag:
    note that there are only three distinct values: 0, 1, and 2
    this allows us to come to the conclusion that if we push all the 0s to the left and all of the 2s to the right  
    we don't need to care about the 1s since they will already we sorted

algorithm:
    1. set a low and mid pointer at index 0 and a high pointer at index -1
        the low pointer and high pointer will be pointers to place the 0s and 2s
        the mid pointer will be used to traverse the array
    2. increment the mid pointer
        if a 0 is encountered, swap the values of the low pointer and mid pointer
            since we don't need to worry about that 0 anymore, we can increment the low pointer
        if a 2 is encountered, swap the values of the high pointer and mid pointer
            since we don't need to worry about that 2 anymore, we can decrement the high pointer
        if a 1 is encountered, we can ignore it
            as long as the 0s and 2s are pushed to the side, the middle of array will contain all of the 1s.

runtime: O(n) mid pointer traverses the array once
space: O(1)


"""


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # dutch national flag problem
    # i got absolutely cooked

    p1 = 0
    p2 = 0
    p3 = len(nums)-1
    while p2 <= p3:
        if nums[p2] == 0:
            nums[p2] = nums[p1]
            nums[p1] = 0
            p1 += 1
            p2 += 1

        elif nums[p2] == 1:
            p2 += 1

        else:
            nums[p2] = nums[p3]
            nums[p3] = 2
            p3 -= 1