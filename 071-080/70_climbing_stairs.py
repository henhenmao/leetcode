
"""
70. Climbing Stairs (https://leetcode.com/problems/climbing-stairs/description/)

this question can easily be done with recursion
    at step n of the stairs, recurse into step n+1 and n+2
        nth stair = n+1th stair + n+2th stair
    every time a recursion branch makes it to the end add 1 to the returned value

the above algorithm will be too inefficient for larger inputs so dynamic programming is required
the reason for this is because this type of recursion leads to many unnecessary repeated operations
    notice that both step n-2 and step n-1 will recurse into step n, and perform the same operation
        climbStairs(n) calls climbStairs(n+1) and climbStairs(n+2)
    these repeating operations will compound as mre steps are made

to solve this problem we use memoization
    create an array of size n called dp
    dp[n] is intended to contain the value of climbStairs(n)
    once climbStairs(n) is first performed, we store that returned value into dp[n]
    this allows us to simply access dp[n] whenever we need to call climbStairs(n) again
        this saves us a crazy amount of time its actually insane how much time is saved

algorithm:
    1. create a dp table of size n
    2. start at stair n and work your way down (other way works too)
        recurse through n-1 and n-2 and return the sum 
        memoize the returned value of dfs(n) into dp[n]
        use dp[n] if it exists else recurse to calculate it
    3. deal with base cases

runtime: O(n) each step is only processed once
space: O(n)

"""


def climbStairs(n: int) -> int:
    # recursively get all distinct ways to climb the stairs
    # use a dp table to memoize each returned distinct count for each cell
    # this will be a top down dp memoize 
    dp = [0] * 50
    count = 0

    def dfs(n): # n = distance from current stair to "top" of stairs
        nonlocal dp

        if dp[n]:
            return dp[n]
        if n <= 2:
            return n

        # memoize the sum of the two possible paths you can take
        dp[n] = dfs(n-1) + dfs(n-2)
        return dp[n]
    
    return dfs(n)