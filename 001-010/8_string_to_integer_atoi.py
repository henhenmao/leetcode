

"""
8. String to Integer (atoi) (https://leetcode.com/problems/string-to-integer-atoi/description/)

rules for atoi(string s):
    1. ignore whitespace
    2. determine positive or negative by checking "+" or "-" (assume positive if neither exist)
    3. skip leading zeros
    4. stop reading when non-digit character or end of string encountered
    5. rounding to [-2^31, 2^31-1] range

how to build integer:
    using "123" as an example:

        result = 0
        when s[i] == "1", multiply the result by 10 and add 1, result = 1
        when s[i] == "2", multiply the result by 10 and add 2, result = 12
        when s[i] == "3", multiple the result by 10 and add 3, result = 123

algorithm:
    1. get through the whitespace
    2. record the positive or negative sign
    3. read the digits one by one and build the integer
        stop reading if non-digit character or end of string
    4. check if number is out of range and round
    5. add the sign at the end if possible    

runtime: O(n) where n is the length of the string
space: O(1)

"""

def myAtoi(s: str) -> int:
    i = 0
    n = len(s)

    # if there is leading whitespace: skip all whitespace
    while i < n and s[i] == " ":
        i += 1

    # see if a sign exists and interpret
    # put both cases into one if statement so you only check for sign one singular time
    sign = 1
    if i < n and (s[i] == "-" or s[i] == "+"):
        if s[i] == "-":
            sign = -1
        i += 1

    # read the characters and build integer one by one
    # stop read if non-digit character is found
    res = 0
    while i < n and s[i].isdigit():
        res = res * 10 + int(s[i])
        i += 1
    
    if res > 2**31-1:
        res = 2**31-1
        if sign == -1: # need to do this since we round to -2^31 not -2^31+1
            res += 1
    
    return sign * res
