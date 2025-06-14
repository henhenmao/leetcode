

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

algorithm:
    1. make an adjacency graph of all the courses
        for each course, list the courses that the course is a prerequisite of
        we will use the course to "unlock" other courses if it is taken
    2. count the indegrees of each course (how many pre-requisites a course has)
        the number of times a course shows up in the adjacency graph is the indegree
    3. find courses that have no indegree (no pre-requisite) (already unlocked)
        add these courses to the taken_courses list and the initial bfs queue
    4. do a bfs to unlock as many courses as you can
    5. for each course in the bfs, decrement each neighboring course's indegree by 1
    6. if a course's indegree becomes 0, it is unlocked and you can add them to the taken_courses and queue
    7. return whether or not all courses are able to be accessed (length of taken_courses == numCourses)

runtime: O(V+E) where V is the number of vertices and E is the number of edges
space: O(V+E) adjacency matrix
"""

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # create a graph adjacency list
    # prerequisite courses are directed to their corresponding courses
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # calculating indegrees of each course and add zero indegrees to initial queue
    # also add zero indegrees to the taken_courses list automatically
    queue = deque([])
    indegrees = [0] * numCourses
    taken_courses = []
    for prereq in graph:
        for course in prereq:
            indegrees[course] += 1

    for course in range(numCourses):
        if indegrees[course] == 0:
            taken_courses.append(course)
            queue.append(course)

    # do the kahn bfs
    while queue:
        curr = queue.popleft()

        # decrement the indegrees of all courses the current course is a prerequisite of
        # if indegree become zero, you take the course and add to the queue
        for course in graph[curr]:
            indegrees[course] -= 1
            if indegrees[course] == 0:
                queue.append(course)
                taken_courses.append(course)

    return len(taken_courses) == numCourses
    
    
# numCourses = 6
# prerequisites = [[1,0],[1,5],[5,4],[2,5],[2,1],[3,2]]
# print(canFinish(numCourses, prerequisites))
        
        



