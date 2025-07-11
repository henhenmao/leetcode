

"""
9. Palindrome Number (https://leetcode.com/problems/palindrome-number/description/)
follow-up: could you solve it without converting the integer to a string?

no string conversion solution:
we want to build a new integer that is the reverse digits of x
    can get the last digit of the x by doing x%10
    can then remove the last digit of x by doing x //= 10

    to make sure each number goes in the right place, we can just multiply the new integer by 10 every
    time we need to add a new digit to the end

    ex. x = 123
        original = 123 (copy of x)
        reverse = 0

        1st iteration:
            remainder = x % 10 -> remainder = 3
            reverse *= 10 -> reverse = 0
            reverse += remainder -> reverse = 3
            x //= 10 -> x = 12
        2nd iteration:
            remainder = x % 10 -> remainder = 2
            reverse *= 10 -> reverse = 30
            reverse += remainder -> reverse = 32
            x //= 10 -> x = 1
        3rd iteration:
            remainder = x % 10 -> remainder = 1
            reverse *= 10 -> reverse = 320
            reverse += remainder -> reverse = 321
            x //= 10 -> x = 0

        once x == 0, compare original to reverse, if they are the same, x is a palindrome
    
"""


def isPalindrome(x: int) -> bool:
    original = x
    reverse = 0

    while x > 0:
        remainder = x%10
        reverse *= 10
        reverse += remainder
        x //= 10
    
    return original == reverse

"""
# this python solution converts x into a string, reverses it, and compares the string to the reverse

def isPalindrome(x: int) -> bool:
    x = str(x)
    return x == x[::-1]
"""
