
from typing import List

"""
3606. Coupon Code Validator (https://leetcode.com/problems/coupon-code-validator/?envType=daily-question&envId=2025-12-14)

just loop from 0 to n and check all the conditions for each coupon

1. code is not empty
2. code is alnumerical with exception to "_"
3. business line is a valid business
4. coupon isActive is true 

put all valid coupons names in a list along with the business name
    put the business name before the coupon name because it should have highest priority when sorting

sort the list and filter out the name only
return the filtered list

runtime: O(n logn)
space: O(n)
"""

def validateCoupons(code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

    n = len(code)
    validBusinesses = ["electronics", "grocery", "pharmacy", "restaurant"]
    validCoupons = []

    for i in range(n):
        currCode = code[i]
        currBusiness = businessLine[i]
        active = isActive[i]

        validCode, validBusiness = False, False

        if currCode and all(c.isalnum() or c == "_" for c in currCode):
            validCode = True

        if currBusiness in validBusinesses:
            validBusiness = True

        if validCode and validBusiness and active:
            validCoupons.append((currBusiness, currCode))

    validCoupons.sort()

    res = [coupon[1] for coupon in validCoupons]
    return res


code = ["SAVE20","","PHARMA5","SAVE@20"]
businessLine = ["restaurant","grocery","pharmacy","restaurant"]
isActive = [True,True,True,True]

print(validateCoupons(code, businessLine, isActive))









