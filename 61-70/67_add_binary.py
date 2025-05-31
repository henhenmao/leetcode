
"""
67. Add Binary (https://leetcode.com/problems/add-binary/description/)

algorithm:
    i just used python to convert each binary number to decimal
    added them and converted back to binary lmao

crazy crutch language

runtime: O(max(n,m)) where n is len(a) and m is len(b)
space: O(max(n,m))
"""

def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]