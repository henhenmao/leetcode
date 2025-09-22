

"""
2785. Sort Vowels in a String (https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2025-09-11)

convert string into a list since strings are immutable

isolate the indices of vowel characters in the string with a list comprehension
    vowel_indices = [i for i, c in enumerate(nums) if c in "AEIOUaeiou"]

create a sorted array of each value of s[i] for each value of i in vowel_indices
    sorted(s[i] for i in vowel_indices) = sorted order of all vowels

match each sorted vowel into the right place back in the original string

runtime: O(n * log(n)) where n is the length of the string
space: O(n)
"""

def sortVowels(self, s: str) -> str:
    s = list(s)
    vowel_indices = [i for i, c in enumerate(s) if c in "AEIOUaeiou"]

    for i, vowel in zip(vowel_indices, sorted(s[i] for i in vowel_indices)):
        s[i] = vowel
    
    return "".join(s)