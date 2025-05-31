


"""
12. Integer to Roman (https://leetcode.com/problems/integer-to-roman/description/)

we can use a greedy solution for this problem:
    find the largest roman value that can be subtracted by the current num
    subtract that amount from the num and add the corresponding roman numeral into the result

the existence of 4 (IV), 9 (IX) and their multiples of ten make our lives slightly harder
    thankfully this problem can easily be fixed in this situation by hard coding the extra values into the list of symbols

runtime: O(1) 1 <= num <= 3999
space: O(1)

"""


def intToRoman(num: int) -> str:
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    a = ""
    i = 0
    while i < 13:
        if num >= values[i]:
            num -= values[i]
            a += symbols[i]
        else:
            i += 1
    return a