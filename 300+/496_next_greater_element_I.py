
from typing import List

"""
496. Next Greater Element I (https://leetcode.com/problems/next-greater-element-i/)

as you go along the numbers in nums2, if the numbers decrease, add values to a stack
    stack will contain encountered values in decreasing order
        top of the stack will contain the smallest element seen so far in the stack

always pop from the stack given the condition that the top of the stack is less than the current value you are iterating at

how to update the correct index when any next greater element is found
    craete a hash map where each value in nums1 is mapped to its index in nums

ex. nums1 = [4,1,2] nums2 = [1,3,4,2]
    initialize stack = [], nums_index = {4:0, 1:1, 2:2}, res=[-1, -1, -1]
    
    i=0, nums2[i]=1, add 1 to top of stack, stack=[1], res=[-1, -1, -1]

    i=1, nums2[i]=3, (nums2[i] > stack[-1]) -> next greatest element is found
        nums_index[stack[-1]] = nums_index[1] = 1 -> update res[1] to nums2[i]
        pop from the stack since stack[-1] was used
        add nums2[i] to the top of the stack

    i=2, nums2[i]=4, add 4 to top of stack, stack=[4], res=[-1, 1, -1]

    i=3, nums2[i]=2, add 2 to top of stack, stack=[4,3], res=[-1, 1, -1]


algorithm:
    1. create nums_index = hashmap where each value that appears in nums1 is mapped to it's index in nums1
    2. create res = result array of all -1s
    3. create an empty stack
    4. iterate through nums2 start to finish

    5. if stack is empty, add the current value if the value is a key in nums_index
        do not add values that do not exist in nums1 into the stack (only those that exist as a key in nums_index)
        skip rest of the iteration if stack is empty
        
    6. if stack is not empty, continue checking whether the current value is greater than the top of the stack
        if true, current value is the next greatest element of the value at top of stack
        get the index that stack[-1] appears in nums by accessing nums_index[stack[-1]]
        update res[nums_index[stack[-1]]] to be set to the current value
        continue this process until the stack empties or the current value is not longer greater than the top of the stack

    7. at end of each iteration, add current value to top of stack ONLY if it exists as a key in nums_index
    8. return result array at the end

runtime: O(n + m) where n is the length nums1 and m is length of nums2
space: O(n)

"""

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    n = len(nums1)
    m = len(nums2)
    
    stack = []
    res = [-1] * n

    nums_index = {}
    for i in range(n):
        nums_index[nums1[i]] = i

    for i in range(m):
        if not stack:
            if nums2[i] in nums_index:
                stack.append(nums2[i])
            continue

        while stack and nums2[i] > stack[-1]:
            res_index = nums_index[stack.pop()]
            res[res_index] = nums2[i]
        
        if nums2[i] in nums_index:
            stack.append(nums2[i])

    return res


nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))
