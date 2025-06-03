


"""
424. Longest Repeating Character Replacement (https://leetcode.com/problems/longest-repeating-character-replacement/description/)

for each character c in the string, we assume that we want to make the entire substring consist of c
keep count of how many times c appears in the window and use pointers to increment
keep count of how many characters in the window that are replacements
    if more replacements than k, iterate the left pointer of the window

runtime: O(n) where n is the length of the string
space: O(n)
"""

def characterReplacement(s: str, k: int) -> int:
    res = 0
    charSet = set(s)

    for c in charSet:
        count = l = 0
        for r in range(len(s)):
            if s[r] == c:
                count += 1

            while (r - l + 1) - count > k:
                if s[l] == c:
                    count -= 1
                l += 1
                
            res = max(res, r - l + 1)
    return res
