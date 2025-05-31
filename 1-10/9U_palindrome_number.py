

"""
9. Palindrome Number (https://leetcode.com/problems/palindrome-number/description/)

follow-up: could you solve it without converting the integer to a string?

i have no words

"""

def isPalindrome(x: int) -> bool:
    x = str(x)
    return x == x[::-1]