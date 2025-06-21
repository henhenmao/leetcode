

"""
5. Longest Palindromic Substring (https://leetcode.com/problems/longest-palindromic-substring/description/)

we can reuse previous palindromes by extending both sides from an already existing palindrone to look for a new one




"""



"""
naive solution:
    below implementation uses a double for loop to get all possible substrings
    checks if substring is a palindrome
    keeps track of the longest palindromic substring

runtime: O(n^3) since for each substring (O(n^2)), you must verify the string for another O(n)
space: O(n)

this solution is crazy slow
"""

"""
def longestPalindrome(s: str) -> str:
        longestStr = 0
        longestLen = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                x = s[i:j]
                if x == x[::-1] and len(x) > longestLen:
                    longestLen = len(x)
                    longestStr = x
        return longestStr
"""

