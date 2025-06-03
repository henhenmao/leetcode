
import unicodedata
from collections import Counter

"""
242. Valid Anagram (https://leetcode.com/problems/valid-anagram/)
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

we can use a hash table and maintain constant space:
    this is because we know that s and t only contain lowercase english letters
        we can create a hash table containing the counts of 26 letters in constant space
    we don't even need to use a hash table just an array is fine too

algorithm:
    1. create two arrays of size 26 to store the letter counts of each string
    2. count each letter in s and t and add the frequencies to the arrays
    3. compare the two frequency arrays

    
runtime: O(n + m) where n is the length of s and m is the length of t
space: O(1)
"""

def isAnagram(s: str, t: str) -> bool:
    count1 = [0] * 26
    count2 = [0] * 26

    for c in s:
        count1[ord(c)-97] += 1
    for c in t:
        count2[ord(c)-97] += 1

    return count1 == count2

"""
follow up:
    i guess we could just use python counter class
    make sure data is normalized so you can get accurate comparisons

runtime: O(n + m)
space: O(n + m)

"""

def isAnagram(s: str, t: str) -> bool:
    count1 = Counter(unicodedata.normalize("NFC", s))
    count2 = Counter(unicodedata.normalize("NFC", t))

    return count1 == count2