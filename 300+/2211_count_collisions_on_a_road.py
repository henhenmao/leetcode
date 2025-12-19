

"""
2211. Count Collisions on a Road (https://leetcode.com/problems/count-collisions-on-a-road/?envType=daily-question&envId=2025-12-04)

all cars will collide except cars on the left edge that go left and cars on the right edge that go right
    given that the cars are not stationary
    count the number of cars that fufill that condition

algorithm:
    1. count the total amount of cars that are not stationary
        upper bound of collisions is all cars that are not stationary

    2. count the number of consecutive cars from the left side that go left
        these cars will never collide into anything since there is nothing on the left to collide into

    3. count the number of consecutive cars from the right side that go right
        same thing as the left

    4. total number of collisions = (all cars are aren't stationary) - (left cars that move left) - (right cars that move right)

runtime: O(n) where n is the length of directions
space: O(1)
"""

def countCollisions(directions: str) -> int:

    n = len(directions)-1

    collisions = 0
    for c in directions:
        if c != 'S':
            collisions += 1

    left_cars = 0
    right_cars = 0
    # count the number of left-moving cars from the left
    for c in directions:
        if c != "L":
            break
        left_cars += 1

    for i in range(n, -1, -1):
        if directions[i] != "R":
            break
        right_cars += 1

    return collisions-left_cars-right_cars