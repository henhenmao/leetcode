

from typing import List
from collections import deque

"""
207. Course Schedule (https://leetcode.com/problems/course-schedule/description/?envType=problem-list-v2&envId=oizxjoit)

kahn's algorithm (bfs):
    1. build an adjacency list for each node and their neighbors
    2. for each node, compute the number of pre-requisites the node has
    3. make a queue starting with nodes that have no prerequisites
    4. while the queue is not empty:
        - curr = queue.pop, add curr to the taken courses
        - for each neighbor of curr, decrease their number of pre-requisites by 1
        - if a node's pre-requisite count becomes 0, add it to the queue
    5. if the taken courses contains all nodes, True, else False

"""

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    pass

    
numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))
        
        



