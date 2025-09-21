

"""
3541. Find Most Frequent Vowel and Consonant (https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/?envType=daily-question&envId=2025-09-13)

have two frequency tables, one for consonants and one for vowels
    after building each hashmap, get the max frequency of each and add them

algorithm:
    1. get the letter frequencies of vowels and consonants in the string
        use two different hashmaps
    2. get the max frequency of each hashmap by looping over each vowel and consonant
    3. return the sum of the two max frequencies

runtime: O(n) where n is the length of the string
space: O(1)    
"""


def maxFreqSum(s: str) -> int:
    vowels = {}
    consonants = {}

    for c in s:
        if c in "aeiouAEIOU":
            d = vowels
        else:
            d = consonants

        if c in d:
            c[d] += 1
        else:
            c[d] = 1

    maxVowels = 0
    maxConsonants = 0
    for n in vowels.values():
        maxVowels = max(maxVowels, n)
    for n in consonants.values():
        maxConsonants = max(maxConsonants, n)

    return maxConsonants + maxVowels