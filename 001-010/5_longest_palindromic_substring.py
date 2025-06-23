

"""
5. Longest Palindromic Substring (https://leetcode.com/problems/longest-palindromic-substring/description/)

i checked out neetcode's solution 
    i'm pretty sure i saw a linear time solution somewhere so i don't think this is compeltely optimal
    i believe it is the intended solution though

we can reuse previous palindromes by extending both sides from an already existing palindrone to look for a new one

for each character in the string, we treat it as the "center" of a palindrome of size 1
    we can continue to check both sides until the palindrome stops being palindromic
        for character at index i, if s[i-1] == s[i+1], you know you have a palindrome of at least length 3
        and just keep going
    keep track of the longest palindrome you find
    you need to check both even and odd palindromes separately

algorithm:
    1. do a loop on every character of string and treat the character as the center
    2. on nums[i], set pointers l and r to both be equal to i
    3. expand pointer l to the left and pointer r to the right, s[l:r+1] is the current substring
    4. as you keep track of s[l:r+1], update the maximum palindromic substring length
    5. continue to expand pointers until s[l] != s[r], because then you know that the current palindrome ends

runtime: O(n^2) where n is the length of the string
space: O(1)

"""
def longestPalindrome(s: str) -> str:
    res = "" # longest palindrome
    maxRes = 0 # length of the longest palindrome

    for i in range(len(s)):

        # checking odd lenght palindromes:
        l, r = i, i
        # while in bounds and left and right pointers are the same
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > maxRes: # if length of the current palindrome is greater than the maximum result:
                res = s[l:r+1]
                maxRes = r-l+1
            l -= 1
            r += 1

        # checking the even length palindromes:
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > maxRes:
                res = s[l:r+1]
                maxRes = r-l+1
            l -= 1
            r += 1
    
    return res
    

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

