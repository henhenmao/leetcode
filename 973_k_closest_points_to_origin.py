
import math
from typing import List
import heapq

"""
973. K Closest Points to Origin

i previously computed the distance for every single point given and turned it into a heap of size n
instead of heapifying all distances, why not just maintain a heap of size k during the iteration of points
that way you can have a space complexity of O(k) instead of O(n)


runtime: O(n * log(n)) where n is the number of points
space: O(k)
"""

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    distances = []

    for x, y in points:
        distance = -math.sqrt(x**2 + y**2) # don't even need to sqrt since the relative distance order is still maintained
        heapq.heappush(distances, (distance, [x, y]))

        if len(distances) > k:
            heapq.heappop(distances)
    
    return [point[1] for point in distances]



"""
algorithm:
    1. convert each point into a distance and turn it into a min heap
        save the actual points in the input along with the corresponding distance
        since each point is relative to (0, 0), you just do distance = math.sqrt(x**2 + y**2) for each point (x, y)
        make sure each distance is negative since you want the highest distances (furthest points) to have priority
    2. keep popping the max distance from the distances until the heap is size k
    3. create a new list of the points remaining and return it

runtime: O(n * log(n))
space: O(n)


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    distances = [[-math.sqrt(x**2 + y**2), [x, y]] for x, y in points]
    heapq.heapify(distances)
    print(distances)

    while len(distances) > k:
        heapq.heappop(distances)
    print(distances)
    

    return [point[1] for point in distances]

"""


# points = [[3,3],[5,-1],[-2,4]]
# k = 2
# print(kClosest(points, k))    