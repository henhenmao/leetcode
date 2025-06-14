
from typing import List
from collections import deque

"""
210. Course Schedule II (https://leetcode.com/problems/course-schedule-ii/)

i don't see any reason not to do the same thing as the first course schedule except just returning a path instead of a True or False
i'm just gonna copy what i did and tweak it a little and see if that works
i just did the first course schedule problem like an hour ago so i'm just gonna rewrite everything again from memory to see if i can

ok i just finished writing the code and turns out you can just copy paste the same thing and change the return value

runtime: O(V + E) where V is the number of vertices and E is the number of edges in the graph 
space: O(V + E) adjacency graph
"""
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # create an adjacency list
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # get the indegrees of each course
    # every course that appears as a neighbor in the adjacency list has an indegree
    indegrees = [0] * numCourses
    
    for prereq in graph:
        for course in prereq:
            indegrees[course] += 1
    
    queue = deque([])
    res = []
    # add zero indegrees to taken_courses and add to the queue as well
    # res will contain our ordered taken courses to return

    for course in range(numCourses):
        if indegrees[course] == 0:
            res.append(course)
            queue.append(course)

    # do bfs
    while queue:
        curr = queue.popleft()
        
        # decremenet all indegrees of curr
        # add unlocked courses to result and queue
        for course in graph[curr]:
            indegrees[course] -= 1
            if indegrees[course] == 0:
                queue.append(course)
                res.append(course)

    if len(res) == numCourses:
        return res
    return []

