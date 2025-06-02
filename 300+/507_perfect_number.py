
import math

"""
507. Perfect Number (https://leetcode.com/problems/perfect-number/description/)

get all the factors of num and exclude num itself from the total sum
if the sum of all the factors - num == num then return true

algorithm:
    1. loop from 1 to sqrt of num so you can get all factors without repeats
    2. if a pair of factors are found add them to the total
    3. return total == num

runtime: O(n^0.5)
space: O(1)
"""

def checkPerfectNumber(num: int) -> bool:
    if num == 1:
        return False

    total = num * -1
    for i in range(1, int(math.sqrt(num)+1)):
        if num % i == 0:
            total += num//i
            total += i
    return num == total