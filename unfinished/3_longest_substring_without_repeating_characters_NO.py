

"""
3. Longest Substring Without Repeating Characters
(https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

i currently have a goofy brute force solution that is very very slow
i have not attempted a linear time solution yet

essentially just for each character in the string:
    see how far you can go without encountering a duplicate
    use a new hash set for each character so you can easily check for duplicates
    keep track of the maximum distance you have travelled from a given character

runtime: O(n^2) for each character you are traversing the entire string
space complexity: O(n) hash set of size n is rebuilt for each character so will hold maximum of n characters
"""

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 1:
        return len(s)

    # use a hash set to detect for duplicates every time
    pivot = 0
    res = 0

    while pivot < len(s):
        i = pivot
        visited = set()
        count = 0
        while i < len(s):
            if s[i] in visited:
                break
            visited.add(s[i])
            count += 1
            i += 1
        res = max(count, res)
        pivot += 1
    return res