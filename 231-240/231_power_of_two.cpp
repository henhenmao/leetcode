

/*
231. Power of Two (https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2025-08-09)
Follow up: Could you solve it without loops/recursion?

binary representations of 2^n
    1 - 1
    2 - 10
    4 - 100
    8 - 1000
first bit is always a 1 and the rest are 0s

binary representations of (2^n)-1
    0 - 0
    1 - 01
    3 - 011
    7 - 0111
first bit is always a 0 and the rest are 1s

notice how if we take a value of 2^n and put it on top of (2^n)-1, each column will contain a single 1 and a single 0
ex. 
    8 and 7 -> 1000
               0111
               
if we take the AND of a valid 2^n and (2^n)-1, we will always get 0 since no column will have two 1s
do not need to worry about negatives since 2^(-n) where n is positive, cannot be an integer
edge case: n = 0, since will compare 0 and 1 and return true since 0 AND 1 = 0

runtime: O(1)
space: O(1)
*/

bool isPowerOfTwo(int n) {
    return n > 0 && (n & n-1);
}