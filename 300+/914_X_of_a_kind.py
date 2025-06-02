

from typing import List
from functools import reduce
import math


"""
914. X of a Kind in a Deck of Cards (https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/)

count the number of each distinct card in the deck 
groups of the same card can be split into two equal groups if needed
essentially need to find a common factor between all distinct group sizes

you could take the minimum group size and check if all group sizes are a multiple
    i think that should work

edit: it did not work when groups were sizes 6 and 8
    i need to get a common factor that can potentially be smaller than the min group

from functools import reduce:
    reduce is a method that applies a function to all list elements in the sequence passed along
    https://www.geeksforgeeks.org/reduce-in-python/
    ex. def add(x, y): 
            return x + y
        a = [1, 2, 3, 4, 5]
        res = reduce(add, a)
        print(res)  # Output: 15
    
    we can use x = reduce(math.gcd, ...) to calculate the greatest common factor of all frequencies in our deck
    if x is greater than 1, we know we can partititon all cards by x

algorithm:
    1. create a dictionary and hash the frequency of each card
    2. as long as the greatest common factor is at least 2, partitioning is possible
    
runtime: O(n)
space: O(n)

"""

def hasGroupsSizeX(deck: List[int]) -> bool:
    groups = {}

    for card in deck:
        if card in groups:
            groups[card] += 1
        else:
            groups[card] = 1

    x = reduce(math.gcd, groups.values()) # kind of cheating?
    if x <= 1:
        return False

    return True