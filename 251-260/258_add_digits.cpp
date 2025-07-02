


/*
258. Add Digits (https://leetcode.com/problems/add-digits/description/)

absolutely vile question 💀

https://en.wikipedia.org/wiki/Digital_root#Direct_formulas
wikipedia page just tells you the answer to the problem but i have no idea why this works


"The digital root (also repeated digital sum) of a natural number in a given radix is the (single digit)
value obtained by an iterative process of summing digits, on each iteration using the result from the
previous iteration to compute a digit sum. The process continues until a single-digit number is reached.
For example, in base 10, the digital root of the number 12345 is 6 because the sum of the digits in the 
number is 1 + 2 + 3 + 4 + 5 = 15, then the addition process is repeated again for the resulting number 15,
so that the sum of 1 + 5 equals 6, which is the digital root of that number. In base 10, this is equivalent
to taking the remainder upon division by 9 (except when the digital root is 9, where the remainder upon
division by 9 will be 0), which allows it to be used as a divisibility rule."

so basically just take the remainder after dividing by 9 and that's the answer
small edge case where n = 9 should return 9 although the remainder is 0

runtime: O(1)
space: O(1)
*/

#include <iostream>
using namespace std;

int addDigits(int num) {
    return 1 + (num-1)%9;
}