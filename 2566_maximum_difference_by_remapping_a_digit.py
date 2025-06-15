

"""
2566. Maximum Difference by Remapping a Digit (https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/?envType=daily-question&envId=2025-06-14)

the biggest impact you can make on a integer num by remapping a digit
    for maximum value: remap the leftmost non-9 digit to a 9
    for minimum value: remap the leftmost digit to a 0

algorithm:
    1. find the leftmost digit for minimum value and the leftmost non-9 digit for the maximum value
    2. iterate through the digits of the integer and create the minimum and maximum values with remapped digits to 9 and 0
    3. find the difference between newly created numbers

runtime: O(n) where n is the number of digits in num
space: O(n)

i jsut did another question and have been made aware of the existence of the replace method in python
would have made my life 10 times easier
"""

def minMaxDifference(num: int) -> int:
    # find the digits
    num = str(num)
    min_digit = num[0]
    max_digit = -1
    for digit in num:
        if digit != "9":
            max_digit = digit
            break

    # build new numbers
    min_num = ""
    max_num = ""
    for digit in num:
        # building minimum
        if digit == min_digit:
            min_num += "0"
        else:
            min_num += digit

        # building maximum
        if digit == max_digit:
            max_num += "9"
        else:
            max_num += digit
    
    return (int(max_num) - int(min_num))

# print(minMaxDifference(99999))

    

