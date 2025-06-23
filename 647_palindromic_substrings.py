


"""
647. Palindromic Substrings (https://leetcode.com/problems/palindromic-substrings/description/)

just do the same thing as 5. Longest Palindromic Substring (https://leetcode.com/problems/longest-palindromic-substring/description/)
but instead of keeping track of the longest palindrome you just count each palindrome you come across
i don't think we need to worry about duplicate values since palindromes of the same length will have different center characters

algorithm:
    1. do a loop on every character of string and treat the character as the center
    2. on nums[i], set pointers l and r to both be equal to i
    3. expand pointer l to the left and pointer r to the right
    4. continue to expand pointers until s[l] != s[r], because then you know that the current palindrome ends
    5. count each palindrome you come across

runtime: O(n^2) where n is the length of the string
space: O(1)
"""

def countSubstrings(s: str) -> int:

    res = 0

    for i in range(len(s)):

        # odd palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        # even palindromes
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

    return res

# s = "aaa"
# print(countSubstrings(s))


        
