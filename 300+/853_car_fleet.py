
from typing import List
import math

"""
853. Car Fleet (https://leetcode.com/problems/car-fleet/description/)

idea:
    form a stack with all cars (position and pseed)
    sort the stack by position of the cars in reverse order
    so that the cars first in line are in priority of the stack
    while there are cars in the stack (not finished)
    take the first two cars and compare them to see if
    the second car will take over the first car
    if yes:
        second car becomes the first car (they merge as one i guess)
    if no:
        first car finishes and count + 1

idea above is the algorithm i don't want to write it all over again

runtime: O(n * log(n)) since we sorted the cars, n is the number of cars
space: O(n)

"""




def carFleet(target: int, position: List[int], speed: List[int]) -> int:

    n = len(position)
    stack = []
    for i in range(n):
        stack.append([position[i], speed[i]])
    stack.sort()

    count = 0
    while len(stack) >= 2:
        a = stack.pop() # first car
        b = stack.pop() # second car

        temp1 = (target-a[0])/a[1]
        temp2 = (target-b[0])/b[1]

        if temp1 < temp2: # first car finishes
            stack.append(b)
            count += 1
        else: # second car catches up
            stack.append(a)

    if stack:
        count += 1

    return count
            