
import heapq
from typing import List

"""
703. Kth Largest Element in a Stream

we need to take advantage of the heap data structure 
    heaps allow us to quickly access the minimum or maximum element

algorithm:
    keep track of the k largest elements we have seen so far
    inserting all elements into a min heap will put the k largest elements in the very end
    if we limit the size of the min heap to only k elements
        a min heap of size k will always have the kth largest element at the very top of it

    just make sure you pop the top of the min heap every time the size exceeds k

why didn't just use sort instead of a heap:
    sorting only gives kth largest element one single time
    since the elements in the heap are constantly changing, sorting every time would be too inefficient

runtime: O(n * log(n)) where n is the number of elemnts in the stream
space: O(n)
"""

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # putting all elements in a minHeap and limiting the size to k
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)