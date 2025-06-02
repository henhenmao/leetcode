
"""
69. Sqrt(x) (https://leetcode.com/problems/sqrtx/)

i actually really like this question i think the solution is kind of cool

algorithm:
    since we know the square root of x is between 1 and x
        we can perform a binary search to search for the square root

    1. set up two pointers low and high at 1 and x
    2. get mid pointer with (low + high)//2
    3. divide x by mid 
        if quotient is equal to mid:
            mid is your perfect square
        if quotient is greater than mid:
            you overshot and need to lower your high pointer
        if quotient is less than midL
            you undershot and need to raise your low pointer
    4. if low == mid, then you have reached the closest integer to the perfect square rounded down

runtime: O(log(x)), since you are performing a binary search on x itself
space: O(1)
"""

def mySqrt(x: int) -> int:
    if x == 0:
        return 0

    low = 1
    high = x

    while True:
        mid = (low + high)//2
        if mid == x/mid or low == mid:
            return mid

        if mid > x/mid:
            high = mid
        elif mid < x/mid:
            low = mid