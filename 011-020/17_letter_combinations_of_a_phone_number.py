from typing import List

"""
17. Letter Combinations of a Phone Number (https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

this is just a combinations problem where we return all combinations from a pool of letters

algorithm:
    1. create a dictionary mapping each number to its phone letters
    2. for each letter in a number group, move onto the next number group and pick a letter from there
    3. step two is done recursively to get all combinations

runtime: O(4^n), where n is the length of digits
    there are a max of four choices to choose from a given letter group
space: O(4^n)

"""

def letterCombinations(digits: str) -> List[str]:
    if digits == "":
        return []

    def aaaa(s, temp):
        if len(s) == 0:
            out.append(temp)
            return
        for c in dict[s[0]]:
            aaaa(s[1:], temp+c)

    dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
    out = []
    aaaa(digits, "")
    return out

# print(letterCombinations("23"))