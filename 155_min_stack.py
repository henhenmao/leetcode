


"""
155. Min Stack (https://leetcode.com/problems/min-stack/description/)
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
You must implement a solution with O(1) time complexity for each function.

when making min stack we create a stack as usual 
    we also have an extra stack to keep track of the current minimum value so we can getMin()

class:
    1. have a stack and mstack
    2. when pushing n to the MinStack, add n to stack, and only add to mstack if the n is less than the top of mstack (mstack[-1])
    3. if n is greater than mstack[-1], simply add mstack[-1] to the top of mstack, since it is the minimum value we have
    4. when popping from the MinStack, just pop from both stacks

runtime: O(1) only taking values from the ends of each stack
space: O(n)

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mstack) == 0 or self.mstack[-1] > val:
            self.mstack.append(val)
        else:
            self.mstack.append(self.mstack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]
        



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()