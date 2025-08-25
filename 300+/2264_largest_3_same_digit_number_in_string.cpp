

/*
2264. Largest 3-Same-Digit Number in String (https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=daily-question&envId=2025-08-14)
A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.

loop through from index 0 to num.length()-1
    if all characters of num.substr(i, 3) are equal to eaach other, current substring of 3 is a good number
    if a good number is encountered, update the current max good number seen so far
    note that you can compare strings based on ascii values so can just do max(maxStr, num.substr(i, 3))

runtime: O(n) where n is the length of num
space: O(1)
*/

#include <iostream>
using namespace std;

string largestGoodInteger(string num) {
    string maxStr = "";

    for (int i = 0; i < num.length()-2; i++) {
        if (num[i] == num[i+1] && num[i+1] == num[i+2]) {
            maxStr = max(maxStr, num.substr(i, 3));
        }
    }    
    return maxStr;
}