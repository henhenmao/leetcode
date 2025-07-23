

"""
231. Power of Two (https://leetcode.com/problems/power-of-two/)
Follow up: Could you solve it without loops/recursion?

recursive/loop solution:
1. repeatedly divide the number by 2
2. if number becomes an odd number before getting to 1, it is not a power of 2

ex. 16 -> 8 -> 4 -> 2 -> 1 -> return true
ex2. 24 -> 12 -> 6 -> 3 -> return false

runtime: O(log(n))
space: O(1)

probably some cheeky bit operation exists that just tells you the answer to this problem idk bit manipultion

"""

def isPowerOfTwo(n: int) -> bool:

    if n <= 0:
        return False
    
    while n > 1:
        if (n % 2 != 0):
            return False
        n /= 2
    
    return True
