
from collections import deque

"""
232. Implement Queue Using Stacks (https://leetcode.com/problems/implement-queue-using-stacks/)
Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

surely the solution will be very similar to the implementing of stacks using two queues
s1 will be the main stack that will represent the queue
s2 will be a stack on standby for when the push function is called

queue functions such as pop(), peek(), and empty() can be easily replaced with
stack pop, stack top and stack empty
main problem is the push function

push(x)
    let s1 = {5,4,3,2,1}, where the end of the list is the top of the stack and the front of the queue
    s1.push(6) should push 6 to the end of the queue, or the bottom of the stack -> {6,5,4,3,2,1}
    since we can only use standard operations of a stack, we need to use the standby stack

    1. move all elements from s1 to s2       s2 = {1,2,3,4,5} and s1 = {}
    2. add 6 to to s1                        s2 = {1,2,3,4,5} and s1 = {6}
    3. move all element from s2 back to s1   s2 = {} and s1 = {6,5,4,3,2,1}

    note that the ordering of the elements were reversed when adding from s1 to s2, but were reversed again and moving back from s2 to s1, so we don't need to worry about that

other functions are trivial


runtime: O(n) for push(), O(1) for all other functions
    where n is the size of the stacks at time of the function call
space: O(n)
"""


class MyQueue:

    def __init__(self):
        self.s1 = deque([])
        self.s2 = deque([])

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s1.append(x)
        
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[0] # i couldn't find a deque top function
        
    def empty(self) -> bool:
        return not self.s1