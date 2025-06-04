

"""
32. Longest Valid Parentheses (https://leetcode.com/problems/longest-valid-parentheses/description/)

when checking for valid parentheses, use the standard stack method

algorithm:
    1. set an array valid = [0] * len(s)
        valid[i] = 1 indicates that s[i] is a part of a valid parentheses

    2. iterate over characters in s

    3. if s[i] == "(", push i the top of the stack

    4. if closing bracket, just check if the stack is empty
        as long as stack isn't empty, we know that the closing bracket is valid
        pop from top of the stack, we now know s[i] and s[stack.pop()] are a parentheses pair
            flip valid[i] and valid[stack.pop()] to equal 1 (valid)

    5. count the consecutive 1's in valid
        longest consecutive sublist of all 1's represents the longest consecutive substring of all valid parentheses
    
runtime: O(n) where n is the length of s
space: O(n) we used a stack
        
"""

def longestValidParentheses(s: str) -> int:
    
    stack = [] # (val, index) pair
    valid = [0] * len(s) # valid[i] means s[i] is a valid parenthes (what is a singular parentheses)

    for i in range(len(s)):
        if s[i] == "(":
            stack.append((i))
        else:
            if len(stack) == 0:
                continue
            valid[i] = 1
            valid[stack.pop()] = 1

    # print(valid)

    # count consecutive 1's in valid array
    res = 0
    curr = 0
    for n in valid:
        if n:
            curr += 1
            res = max(res, curr)
        else:
            curr = 0

    return res