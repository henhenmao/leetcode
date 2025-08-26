

"""
205. Isomorphic Strings (https://leetcode.com/problems/isomorphic-strings/description/)

store the first index where each distinct character was seen in hashmap first_index
for each character in the string
    if it's the first time seeing the character c:
        store the i index to first_index[c]
    add first_index[c] to an output list
        we will compare the output lists of s and t

storing the first seen index of each character in both strings will let us know if two strings have the same isopmorphic pattern

runtime: O(n)
space: O(n)
"""

def isIsomorphic(s, t):
    def pattern(s):
        first_index = {}
        out = []
        for i, ch in enumerate(s):
            if ch not in first_index:
                first_index[ch] = i
            out.append(first_index[ch])
        return out

    return pattern(s) == pattern(t)

print(isIsomorphic("foo", "bar"))