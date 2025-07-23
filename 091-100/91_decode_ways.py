

"""
91. Decode Ways (https://leetcode.com/problems/decode-ways/?envType=problem-list-v2&envId=oizxjoit)

this may just be a dfs/dynamic programming question kind of like climbing stairs or house robber
if you encounter a 1 or a 2, you can either interpret it as a single number or the beginning of a two digit number

ex. s = "12345"
    s[0] = "1" can be decoded as "1" = "A" or a part of "12" = "L"

notes: 
    kind in mind that if there are adjacent 1s or 2s you must avoid doing repeating two digit number beginnings
        just skip the next number if you ever encounter a 1 or 2 and choose to make it a double digit
    zeros can only be used as the second number of a double digit
        since all zeros should be skipped due to the above rule, we can just return 0 when any zero is encountered
    last niche case is the fact that we cannot have 27, 28, 29
        we can just check s[i+1] if s[i] is a 2 and ignore values of 7, 8, and 9

algorithm:
    1. for each digit, if not a 1 or a 2, recurse to the next digit
    2. if s[i] is a 1, recurse to s[i+1] as a "1" and recurse to s[i+2] as a "10"
    3. if s[i] is a 2, check that next digit is not a 7, 8, or 9 and recurse to s[i+1] as a "2" and to s[i+2] as a "20"
    4. memoize all return values since the numbers get very big

runtime: O(n) where n is the length of the string
space: O(1)

"""

def numDecodings(s: str) -> int:

    n = len(s, )
    res = 0 # count the number of decodings
    valid_numbers = ["0","1","2","3","4","5","6"]
    dp = [0] * (n+1)

    def dfs(i):
        nonlocal res

        # base case: reached the end of the string
        if i >= n:
            return 1
        
        if dp[i]:
            return dp[i]
        
        if s[i] == "0":
            dp[i] = 0
            return 0
        
        dp[i] = dfs(i+1)
        if i < n-1 and (s[i] == "1" or (s[i] == "2" and s[i+1] in valid_numbers)):
            dp[i] += dfs(i+2)        

        return dp[i]
    return dfs(0)