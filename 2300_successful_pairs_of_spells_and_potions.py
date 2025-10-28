
from typing import List
import bisect

"""
2300. Successful Pairs of Spells and Potions (https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=daily-question&envId=2025-10-04)

we want to return an integer array pairs where pairs[i] is the number of potions that will form succesfully with the ith spell
    this means that for every individual spell, we want to find the number of potions

sort the potions array
    if spells[i] is successful with potions[j], then spells[i] will be succesful for potions[j+1], potions[j+2]..... 

for each spell, do a binary search / bisect on the sorted potions array
    find the first j value where potions[j] * spells[i] is at least success

bisect:
    we want to find spells[i] * potions[j] >= success
    for each spells[i], we want to find potions[j] that are at least success/spells[i]
    use bisect to find the first occurence of this


algorithm:
    1. sort the potions array
    2. create pairs array that will be returned at the end
    3. for each spell, do a binary search on potions
        find the first index of j where potions[j] * spell[i] is greater than or equal to success
    4. once j is found, we know that all indices after j will also lead to valid successful pairs
        let m be the length of potions, the ith spell will have (m-j) successful pairs

runtime: O(n * logm + m * logm) where n is the length of spells and m is the length of potions
space: O(n)
"""

def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:

    pairs = []
    potions.sort()
    n = len(potions)

    for spell in spells:
        minStrength = success/spell # spells[i] is at least 1
        i = bisect.bisect_left(potions, minStrength)
        numPotions = n-i
        pairs.append(numPotions)

    return pairs

spells = [3,1,2]
potions = [8,5,8]
success = 16
    
print(successfulPairs(spells, potions, success))