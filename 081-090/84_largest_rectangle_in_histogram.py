
from typing import List


"""
84. Largest Rectangle in Histogram (https://leetcode.com/problems/largest-rectangle-in-histogram/)

i found this question so challenging that i had to watch a NeetCode explanation video about the solution
ain't no way i'm coming up with a solution like this mid-interview
never in a million years

we need to use a stack for this question
    when a bar is shorter than the one on top of the stack, the bar on top of the stack essentially cannot extend any further
    therefore we must pop the bar on top of the stack and replace it with the shorter one
        we also should set the shorter bar's start index to the start index of the popped bar
            since we know that the shorter bar can extend backwards to the beginning of the taller bar
    if bars are in increasing order, just add to the stack

after traversal, there will be some remaining bars thta we must check the area of
    thankfully it's really simple as we just take every bar and calculate its area as its height * len(heights)

algorithm:
    1. create maxArea and stack
    2. iterate through each bar in heights and keep track of its index and height
    3. for each bar, if the height is greater than or equal to the top of the stack, add it to the top of the stack and move on
    4. if the height of the bar is less than the top of the stack, we do the following:
        - pop from the top of the stack
        - calculate the maxArea that the popped bar could have made
        - set the new bar's starting index to the popped bar's index
    5. after traversal, calculate the max areas of the remaining bars left in the stack

runtime: O(n) where n is the length of heights
space: O(n)


"""


def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = [] # (index, height)

    for i, h in enumerate(heights):
        
        # set start index of current height
        # because don't know if can extend backwards
        start = i

        # if current height is less than the previous height:
        # we need to pop from the stack and calculate the area
        while stack and stack[-1][1] > h:
            index, height = stack.pop() # index and height of most recent height in stack
            maxArea = max(maxArea, height * (i-index))
            start = index

        stack.append((start, h))

    # print(stack)

    # dealing with elements remaining in stack after end of traversal
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
        # print(h * (len(heights) - 1))

    return maxArea