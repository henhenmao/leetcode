
/*
326. Power Of Three (https://leetcode.com/problems/power-of-three/)
Follow up: Could you solve it without loops/recursion?

used recursive function to keep dividing n by 3 until either cannot divide by 3 (returns false) or reaches 1 (true)

don't know how to solve without loops/recursion
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