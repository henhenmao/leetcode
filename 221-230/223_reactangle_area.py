
"""
223. Rectangle Area (https://leetcode.com/problems/rectangle-area/)

find the horizontal and vertical overlap between the two rectangles
multiply them together to get the intersect

x-overlap:
    we can check for an overlap in the x-axis by comparing the rightmost left side and the leftmost right side
    rightmost left side = max(ax1, bx1)
    leftmost right side = min(ax2, bx2)
    if the rightmost left side is less than the leftmost right side, you know there is an overlap between the two rectangles

y-overlap
    we can check for an overlap in the y-axis by comparing the highest bottom side and the lowest top side

it's really easy if you just draw it on a piece of paper
union area covered = area1 + area2 - intersection

algorithm:
    1. calculate the overlap of the two rectangles in the x axis and y axis
    2. if the interval of the overlap is negative, there is no overlap -> total intersect = 0
    3. add the two areas and subtract the intersection to get the union area

runtime: O(1)
space: O(1)


"""

def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    overlapX = [max(ax1, bx1), min(ax2, bx2)]
    overlapY = [max(ay1, by1), min(ay2, by2)]

    if overlapX[0] > overlapX[1] or overlapY[0] > overlapY[1]:
        intersect = 0
    else:
        intersect = (overlapX[1]-overlapX[0]) * (overlapY[1]-overlapY[0])

    res = (ax2-ax1) * (ay2-ay1) + (bx2-bx1) * (by2-by1) - intersect
    return res