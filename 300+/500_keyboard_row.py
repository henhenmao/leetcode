
from typing import List

"""
500. Keyboard Row (https://leetcode.com/problems/keyboard-row/description/)

this is a problem that requires hash sets

algorithm:
    1. create hash sets contain each row of the keyboard
    2. for each word in words, find the keyboard row that matches with the first character of word
    3. just iterate for the rest of the word and make sure each remaining letter matches with the same row
        very easy to match since there are only three rows
    4. if a single letter does not match then it is not valid
    5. add all valid words into result and return

runtime: O(n*m) where n is the length of words, and m is the average length of each word in words
space: O(n)
"""


def findWords(words: List[str]) -> List[str]:
    row1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
    row2 = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
    # row3 = {"z", "x", "c", "v", "b", "n", "m"}

    res = []

    for word in words:
        curr = word[0].lower()
        if curr in row1: row = 1
        elif curr in row2: row = 2
        else: row = 3

        yes = True
        i = 1
        while i < len(word):
            curr = word[i].lower()
            if curr in row1: temp = 1
            elif curr in row2: temp = 2
            else: temp = 3
            if row != temp:
                yes = False
                break
            i += 1
        
        if yes:
            res.append(word)
    
    return res