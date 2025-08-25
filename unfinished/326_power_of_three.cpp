
/*
326. Power Of Three (https://leetcode.com/problems/power-of-three/)
Follow up: Could you solve it without loops/recursion?

math solution:
    3^19 is the largest power of three below 2^31
        since 3 is a prime number, that means the its only factors are powers of three
    any number that divides perfectly into 3^19, is a power of three

runtime: O(1)
space: O(1)
*/

#include <iostream>
using namespace std;

bool isPowerOfThree(long n) {
    return n > 0 ? ((long)(pow(3, 19)) % n == 0) : false;
}


/*
recursive solution
used recursive function to keep dividing n by 3 until either cannot divide by 3 (returns false) or reaches 1 (true)

runtime: O(log_3(n))
space: O(1)
*/

bool recur(long n) {
    if (n == 1) {
        return true;
    }
    if (n % 3 != 0) {
        return false;
    }
    return recur(n/3);
}

bool isPowerOfThree(long n) {
    if (n <= 0) {
        return false;
    }
    return recur(n);
}