
"""
50. Pow(x, n) (https://leetcode.com/problems/powx-n/)

easy solution
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
kidding

binary exponentiation: https://cp-algorithms.com/algebra/binary-exp.html 
bro i would never come up with something like this in an interview if they asked me this

binary exponentiation:
    instead of a O(n) x^n where we multiply x by itself n times,
    we can convert n to binary, where the length of binary(n) is log2(n)
    we can then calculate the powers of the log2(n) binary digits instead of n

given b^x:
    b^x = b^(2 * x//2)
    b^x = b^(2 * x//2) = (b^2)^(x//2)

because of the above property, we can continue to divide the exponent by two
    every time we do this we square the current value of the base

if the exponent is an odd number, we can just multiply by the base one time
    essentially subtracting the exponent value by 1


algorithm:
    1. return 1 if the exponent is 0
    2. if exponent is negative, change base to equal its reciprocal
    3. continue to halve the exponent n and square the current result of x until n = 0
    4. if n is an odd number, just multiply the result by x once

runtime: O(logn)
space: O(1)

"""

def myPow(x: float, n: int) -> float:
    
    # anything to the power of 0 = 1
    if x == 0:
        return 1
    
    # change the base to its reciprocal if the exponent is negative
    if n < 0:
        x = 1/x
        n = -n

    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= x
        x *= x
        n //= 2
    return res
