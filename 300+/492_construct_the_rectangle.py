import math
from typing import List

"""
492. Construct the Rectangle (https://leetcode.com/problems/construct-the-rectangle/description/)

rules of question:
    1. The area of the rectangular web page you designed must equal to the given target area.
    2. The width W should not be larger than the length L, which means L >= W.
    3. The difference between length L and width W should be as small as possible.


given an area, we need to find the factors of the area and test factor pairs if they follow the conditions
i don't know if condition 2 ever matters as long as your factor pairs are in non descending order

algorithm:
    1. return the first factor pair starting from sqrt(area) and going down to 0
        we can just return the first one we see since the factor closest to sqrt(area) is guaranteed
        to have the smallest difference between the two factors

runtime: O(n^0.5) where n is the area
space: O(1)
"""

def constructRectangle(area: int) -> List[int]:
    for i in range(int(math.sqrt(area)), 0, -1):
        if area % i == 0:
            return [area // i, i]
        


"""
my previous algorithm (naive?):
    1. find all factors pairs of the area and put each pair in a big array
    2. sort the array based on the difference between the pairs
    3. return the first pair (will have smallest difference)

runtime: O(n * log(n)) where n is the area given
space: O(n^0.5)
"""
def constructRectangle(area: int) -> List[int]: 
    pairs = []
    for i in range(1, int(math.sqrt(area)+1)):
        if area % i == 0:
            pairs.append([area // i, i])

    pairs.sort(key=lambda x: (x[0]-x[1]))
    print(pairs[0])