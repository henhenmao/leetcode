


"""
13. Roman to Integer (https://leetcode.com/problems/roman-to-integer/description/)

things to note:
    using XIX (9) as an example, off first glance we would split it into X and IX and calculate 10 + 9
    notice how IX is essentially X - I = (10 - 1) = 9
    the same can see seen with XL (fourty)
        L - X = (50 - 10) = 40 

    since roman numerals always go down in descending order:
        we only need to do this subtracting thing when we encounter a value that is less than the value after it

algorithm:
    for each character in the roman numeral x[i], check the value in front of it x[i+1]
    if x[i] < x[i+1]:
        we know that we need to subtract x[i+1] by x[i] to get the value

runtime: O(n) where n is the length of x
space: O(1)
"""


def romanToInt(x : str) -> int:
    values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = values[x[-1]]
    for i in range(len(x)-1):
        temp = values[x[i]]
        temp2 = values[x[i+1]]
        if temp < temp2:
            total -= temp
        else:
            total += temp
    return total

# print(romanToInt("IV"))