
from typing import List

"""
31. Next Permutation (https://leetcode.com/problems/next-permutation/description/)
The replacement must be in place and use only constant extra memory.

need to find the next larger number 
meaning we probably only need to make a single swap within nums
we just need to find which two numbers in nums to swap

finding the next permutation:
    start by looking at the last digit of nums (i = len(nums)-1)
        if nums[i-1] is less than nums[i], you can just swap the two
            ex. nums = [1,2,3] -> [1,3,2]

    if nums[i-1] is greater than nums[i], look at nums[i-2], keep going down nums until nums[i-j] is less than nums[i]
        swap nums[i-j] and nums[i], and sort all values to the right of nums[i-j]
            ex. nums = [1,2,5,4,3] -> swapping index 4 and index 1 -> [1,3,5,4,2] -> sorting all values to right of index 1 -> [1,3,2,4,5] = next perm

    i have no idea on how to implement this mainly the sorting part maybe just bubble sort it since it uses contant space
        runtime would be O(n^2) then if a bubble sort
        i'll try it


    this question is not possible

"""

def nextPermutation(nums: List[int]) -> None:
    i = len(nums)-1
    j = len(nums)-2

    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    while j >= 0:
        if nums[j] < nums[i]:
            break
        j -= 1

    swap(i, j)

    # doing a BUBBLE SORT LMAO 😂
    j += 1
    
    for n in range(i, j, -1):
        swapped = False
        for k in range(n):
            if nums[k] > nums[k+1]:
                swap(k, k+1)
                swapped = True
        if not swapped:
            break
    

        # print(j)
# nums = [2,3,1]
# nextPermutation(nums)
# print(nums)

        


