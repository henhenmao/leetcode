
from typing import List

"""
238. Product of Array Except Self
You must write an algorithm that runs in O(n) time and without using the division operation.
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

main idea:
    assuming a perfect world where there are no zeros in the array:
        let k be the product of every single element in the array (ex. nums = [1,2,3,4,5], k = 120)
        for each value of nums[i], we simply need to change it to k//nums[i]
            this will give us the product of every element except for nums[i]

concerning zeros:
    - if there is one zero in the array, all other elements' products will include 0 and become 0 (except for the zero itself)
    - if there are two or more zeroes in the array, every element's product will include a 0 and become 0
    ex. [1,2,0,3,4,5] -> [0,0,120,0,0,0]
        [1,2,0,0,4,5] -> [0,0,0,0,0,0]

algorithm:
    we just need to count the number of zeros in the array at the beginning
    at the same time we calculate k, total product of the array excluding zeros

    if there are 2 or more zeros:
        return an array of all [0]
    if there is only 1 zero:
        return an array of all [0] except for the product of array on the index containing the single zero

    if no zeros exist:
        just set each nums[i] in the array to k//nums[i]

runtime: O(n)
space: O(n) (O(1) if we exclude the output array)
"""

def productExceptSelf(nums: List[int]) -> List[int]:
    nums_product = 1
    zeros = 0
    for i in nums:
        if i != 0:
            nums_product *= i
        else:
            zeros += 1
    if zeros > 1:
        return [0] * len(nums)

    res = []
    for i in nums:
        if zeros > 0:
            if i == 0:
                res.append(nums_product)
            else:
                res.append(0)
        else:
            res.append(nums_product // i)

    return res