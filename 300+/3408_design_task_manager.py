
from typing import List
import heapq

"""
3408. Design Task Manager (https://leetcode.com/problems/design-task-manager/description/?envType=daily-question&envId=2025-09-17)

have a hashmap that contains pairs of taskId : (userId, priority)


have a single max heap structure that contains the data for each person (priority, taskId, userId)
    this allows the execTop() function to pop from the top of the heap and return the userId

TaskManager()
    initialize a hashmap and heapq
    add key value pairs of taskId : (userId, priority, False) to the hashmap
        the False is a marker for whether or not the task with taskId was removed with the rmv function
    add each (-priority, -taskId, userId) to the heap
        prioritize the max priority and max taskId

add()
    create a new taskId task in the hashmap
    add a new (-priority, -taskId, userId) to the heap

edit()
    using the hashmap, update the priority of the taskId key
    create a new task with (-newPriority, -taskId, userId) and add it to the heap

rmv()
    mark the hashmap element with key taskId as deleted = True

execTop()
    keep popping from the heap until you get to a task that exists in taskMap and is not marked as removed
    remember to remove the task from the hashmap too before returning the userId

runtime:
    TaskManager(): O(n) where n is the number of inital tasks
    add(): O(1)
    edit(): O(1)
    rmv() O(1)
    execTop(): O(log n)w

space: O(n)
"""

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskMap = {}
        self.taskHeap = []

        for userId, taskId, priority in tasks:
            self.taskMap[taskId] = [userId, priority, False]
            heapq.heappush(self.taskHeap, (-priority, -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = [userId, priority, False]
        heapq.heappush(self.taskHeap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        task = self.taskMap[taskId]
        task[1] = newPriority
        heapq.heappush(self.taskHeap, (-newPriority, -taskId, task[0]))

    def rmv(self, taskId: int) -> None:
        self.taskMap[taskId][2] = True

    def execTop(self) -> int:
        while self.taskHeap:
            priority, taskId, userId = heapq.heappop(self.taskHeap)
            if -taskId in self.taskMap and self.taskMap[-taskId] == [userId, -priority, False]:
                self.taskMap[-taskId][2] = True
                return userId
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()