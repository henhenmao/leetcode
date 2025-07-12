

/*
414. Third Maximum Number (https://leetcode.com/problems/third-maximum-number/description/)
Follow up: Can you find an O(n) solution?

pass through the array to get the maximum number (or just use max() actually)
pass through the array again to get the second maximum number (greatest value that isn't equal to the max value)
pass through the array again to get the third maximum number (greatest value that isn't equal to the max value or the second max value)

set a boolean to make sure that a third value actually exists

runtime: O(n) where n is the length of nums
space: O(1)
*/

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int thirdMax(vector<int>& nums) {
    
    int firstMax = INT_MIN;
    int secondMax = INT_MIN;
    int thirdMax = INT_MIN;
    bool thirdValueExists = false;

    // first max
    for (int n : nums) {
        firstMax = max(firstMax, n);
    }

    // second max
    for (int n : nums) {
        if (n != firstMax) {
            secondMax = max(secondMax, n);
        }
    }

    // third max
    for (int n : nums) {
        if (n != firstMax && n != secondMax) {
            if (n > thirdMax) {
                thirdMax = n;
                thirdValueExists = true;
            }
        }
    }

    return thirdValueExists ? thirdMax : firstMax;
}