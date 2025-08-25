

"""
1323. Maximum 69 Number (https://leetcode.com/problems/maximum-69-number/?envType=daily-question&envId=2025-08-16)

we change one digit only not all instances of a 6 or a 9
    misread the question :(

question is somewhat misleading as you never want to change a 6 to a 9 ever because that makes the number smaller
    we want to the find the best 6 digit to change to a 9
    just find the first 6 digit because that has the highest place in the number

algorithm:
    1. convert num to a list of each digit
    2. find the first '6' digit and change it to a '9'
    3. convert the list back into an integer

runtime: O(n) where n is the number of digits in num
space: O(n)
"""

def maximum69Number (num: int) -> int:
    s = list(str(num))
    for i in range(len(s)):
        if s[i] == '6':
            s[i] = '9'
            return int(''.join(s))
    return int(''.join(s))
