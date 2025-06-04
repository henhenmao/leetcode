
from typing import List

"""
271. Encode and Decode Strings (https://neetcode.io/problems/string-encode-and-decode?list=blind75)
this was a problem in NeetCode roadmap and is locked behind premium in LeetCode (tragic)

this is a very interesting problem

dude i do NOT want to comment this code
looks like a mess

"""


def encode(strs: List[str]) -> str:
    res = ""
    for word in strs:
        res += str(len(word)) + "#"
        res += word
    return res

def decode(s: str) -> List[str]:
    res = []
    word = ""
    i = 0
    newWord = True
    n = ""
    sz = 0
    while i < len(s):
        if newWord:
            if s[i] != "#":
                n += s[i]
                i += 1
                continue
            sz = int(n)
            newWord = False
            
        for _ in range(sz):
            i += 1
            word += s[i]

        i += 1
        newWord = True
        res.append(word)
        word = ""
        n = ""

    return res