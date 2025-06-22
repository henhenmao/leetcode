
from typing import List

"""
2138. Divide a String Into Groups of Size k (https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/?envType=daily-question&envId=2025-06-22)


algorithm:
    1. start with two pointers i and j at index 0
        s[i:j] will be a group of size k
    2. increment j until it becomes k larger than i
    3. when that happens take s[i:j] and add to the result
    4. add j to i to set a new starting point for the next group of s[i:j]
    4. if the end of the string is reached by j, fill the rest of the group with fill variable
        just do (fill * (k-j)) to get the right amount of fills

runtime: O(n) where n is the length of s
space: O(n)
"""

def divideString(s: str, k: int, fill: str) -> List[str]:
    res = []

    n = len(s)
    i = 0   
    j = 0
    while i < n:
        if i+j == n:
            res.append(s[i:i+j] + (fill * (k-j)))
            break

        elif j >= k:
            res.append(s[i:i+j])
            i += j
            j = 0
        else:
            j += 1
    return res
        
        
        
# s = "abcdefghij"
# k = 3
# print(divideString(s, k, "n"))