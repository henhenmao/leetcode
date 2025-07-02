
from typing import List

"""
189. Rotate Array (https://leetcode.com/problems/rotate-array/description/)
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

constant space in place algorithm: 
    do the exact same thing but manually reverse the list using your own function


runtime: O(n)
space: O(1)

"""

def rotate(nums: List[int], k: int) -> None:

    # swaps index i and j in nums
    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    # reverses the sublist of nums[i:j+1]
    def reverseList(i, j):
        while i < j:
            swap(i, j)
            i += 1
            j -= 1
    
    n = len(nums)
    k %= n
    reverseList(0, n-1)
    reverseList(0, k-1)
    reverseList(k, n-1)

# nums = [1,2,3,4,5,6,7]
# rotate(nums, 3)
# print(nums)


"""
algorithm:
    1. take the mod of k and len(nums) since rotating the array len(nums) times gives the same array
    2. reverse nums
    3. reverse the sublist up to k
    4. reverse the sublist from k to the end

ex. nums = [1,2,3,4,5,6,7], k = 3
    1. k = 3
    2. nums = [7,6,5,4,3,2,1]
    3. nums = [5,6,7,4,3,2,1]
    4. nums = [5,6,7,1,2,3,4]

according to chatgpt the reversed() function actually isn't O(n) space complexity but actually O(1)
not sure though 

runtime: O(n)
space: O(n) - can be improved
"""

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    k %= len(nums)
    nums.reverse()

    nums[k:] = reversed(nums[k:])
    nums[:k] = reversed(nums[:k])