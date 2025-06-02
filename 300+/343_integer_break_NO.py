


"""
343. Integer Break (https://leetcode.com/problems/integer-break/description/)

dp[i] will store the maximum product you can get by breaking the number i
for each i from 2 to n, we consider all possible first parts

we explore the two cases:
    1. not breaking the second part: j * (i-j)
    2. breaking the second part recursively: d * dp[i-j]
we take the maximum of these two update dp[i]

runtime: O(n^2)
space: O(n)

apparently there is a linear runtime solution to this problem but i have no idea what it is
"""

def integerBreak(n: int) -> int:

    dp = [0] * n+1 # index = sum left
    for i in range(2, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
    return dp[n]