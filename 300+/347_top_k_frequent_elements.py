
from typing import List
import heapq

"""
347. Top K Frequent Elements (https://leetcode.com/problems/top-k-frequent-elements/description/?envType=problem-list-v2&envId=oizxjoit)

get the frequency of each element in a hash map
put each element-frequency pair into a minheap of size k
if the size of the heap ever exceeds k, we pop from the top of the heap (the minimum frequency)

algorithm:
    1. count frequencies of each element in nums
    2. add all frequency element pairs into a minheap, with the frequency having priority
    3. if the heap size exceeds k, pop the head of the heap
    4. return a list of all elements in the remaining heap of size k

runtime: O(n * log(k)) where n is the size of nums
space: O(n)
"""

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else: 
            freq[n] = 1

    heap = []
    for n, count in freq.items():
        heapq.heappush(heap, (count, n))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [n for count, n in heap]
  

