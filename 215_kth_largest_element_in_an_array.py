
from typing import List
import heapq

"""
215. Kth Largest Element in an Array (https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

algorithm:
    1. create min heap and set to prioritize max values by negativing all elements
    2. add all values in nums into the priority queue
    3. remove the head of the heap k-1 times
    4. return the head of the heap 

runtime: O(n * log(k)) a priority queue takes log(k) time to insert items into a queue of size k
    we are doing a log(k) insertion for every elemenet in nums 
space: O(k) storing k elements at most
"""

def findKthLargest(nums: List[int], k: int) -> int:
    nums = [-n for n in nums]
    heapq.heapify(nums)

    for _ in range(k-1):
        heapq.heappop(nums)
    
    return -heapq.heappop(nums)

# print(findKthLargest([3,2,1,5,6,4], 2))



