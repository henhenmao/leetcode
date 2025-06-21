
import heapq
from typing import List

"""
1046. Last Stone Weight

use a max heap for this problem
convert stones into a max heap and runt he simulation described in the problem

i wasn't sure how to make a max heap so i just used a min heap with all stone values flipped to negative values

algorithm:
    1. multiply every stone's value by -1
    2. heapify the stones into a min heap
    3. run the simulation while the size of stones is greater than 1
        a. pop the top two values of the heap (two heaviest stones)
        b. compare the two
        c. subtract the heavier stone by the other stone
        d. do nothing if they are equal

runtime: O(n * log(n))
space: O(n)
"""

def lastStoneWeight(stones: List[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        stone1 = heapq.heappop(stones)
        stone2 = heapq.heappop(stones)
        
        if stone1 < stone2:
            stone1 -= stone2
            heapq.heappush(stones, stone1)
        
        elif stone2 < stone1:
            stone2 -= stone1
            heapq.heappush(stones, stone2)
        
    if len(stones) == 1:
        return heapq.heappop(stones) * -1
    return 0

# stones = [2,7,4,1,8,1]
# print(lastStoneWeight(stones))