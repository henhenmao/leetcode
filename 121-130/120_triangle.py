
from typing import List

"""
120. Triangle (https://leetcode.com/problems/triangle/description/)
Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?

this question is very similar to another problem but with a rectangle instead of a triangle
    i think it was this one 64. Minimum Path Sum https://leetcode.com/problems/minimum-path-sum/description/

you pretty much do the exact same thing as minimum path sum but take into account the shape of the triangle when traversing

algorithm:
    1. create a dp table (the length of triangle is len(triangle[-1]) since its the longest side)
    2. when at triangle[i][j], look at triangle[i-1][j] and triangle[i][j-1] and tabulate for the minimum path
    3. just make sure you don't go out of bounds since it's really easy with a triangle

runtime: O(n^2) where n is the number of rows in the triangle
space: O(n^2)

"""

def minimumTotal(triangle: List[List[int]]) -> int:
    dp = [[-1 for _ in range(len(triangle[-1]))] for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        dp[i][0] = triangle[i][0] + dp[i-1][0]

    for j in range(1, len(triangle[-1])):
        dp[j][j] = triangle[j][j] + dp[j-1][j-1]

    for i in range(2, len(triangle)):
        if i >= len(triangle):
            continue
        for j in range(1, len(triangle[i])):
            if j >= len(triangle[i])-1:
                break
            dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
            # dp[i][j] = 100

    return min(dp[-1])