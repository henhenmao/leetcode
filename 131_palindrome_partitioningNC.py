
from typing import List

"""
131. Palindrome Partitioning (https://leetcode.com/problems/palindrome-partitioning/description/)

neetcode helped me with this problem 

getting all partitions in the string
    split the current string s into s[:i] and s[i:]
    make sure s[:i] is a palindrome is well, if not the backtrack
    recursively call for partitions in s[i:] 

algorithm:
    1. for the string s, take every substring from i to j
    2. prune the cases of non-palindromic substrings by checking if s[i:j+1] is a palindrome or not
    3. if the substring is palindromic, recurse into the right side for more palindromes
    4. if your index makes it to the end of the s, you know you have a palindromic partition

runtime: O(n * n^2) where n is the length of the string
    getting partitions takes O(2^n) time and checking palindromes is O(n)

space: O(n) partition size at most

"""

def partition(s: str) -> List[List[str]]:

    # functions that returns whether a given string is palindromic or not
    def isPalindrome(s: str):
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    res = []
    curr = [] # current partition

    def dfs(i):
        # base case:
        # if you reach the last index you know everything is a palindrome 
        if i >= len(s):
            res.append(curr[:])
            return
        
        # generating every substring from i to j
        # skipping non palindromes
        for j in range(i, len(s)):
            if isPalindrome(s[i:j+1]):
                curr.append(s[i:j+1])
                dfs(j+1)
                curr.pop()

    dfs(0)
    return res