




"""
1432. Max Difference You Can Get From Changing an Integer (https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/?envType=daily-question&envId=2025-06-15)
Note that neither a nor b may have any leading zeros, and must not be 0.

let a be the integer after changing it once, and b be the integer after changing it for the second time

we should try two things:
    minimum a value and maximum b value
    maximum a value and minimum b value

see which of these two scenarios gives the maximum difference between a and b and return it

omg i should read the quesiton properly next time jesus
i hate this quesrtuo so mcuhfaiosdnfijasdiuof iufhsaiu


algorithm: 
    1. set functions to get maximum of num and the minimum of num
    2. maxNum function just finds the leftmost non-9 digit as usual and returns a num with all instances of that digit replaced with "9"
    3. minNum function can't return with leading zeros so there are a bunch of edge cases
        - if the first digit of num is not "1", we can just set it to 1 and that is our minimum
        - if the first digit is 1, we find the leftmost digit that is not 0 or 1
            - not 0 since we can't decrease it any further
            - not 1 since the digit 1 is one and replacing it to 0 will give us a leading zero
    4. return the difference between the maxNum(num) and minNum(num)

runtime: O(n) where n is the number of digits in num
space: O(n)

"""

def maxDiff(num: int) -> int:
    
    def maxNum(num):
        for c in num:
            if c != '9':
                return num.replace(c, '9')
        return num
    
    def minNum(num):
        if num[0] != "1":
            return num.replace(num[0], "1")
        for c in num[1:]:
            if c != "0" and c != "1":
                return num.replace(c, "0")
        return num

    num = str(num)
    print(maxNum(num))
    print(minNum(num))
    return (int(maxNum(num)) - int(minNum(num)))

# 9901057-1101007
# print(maxDiff(1101057))