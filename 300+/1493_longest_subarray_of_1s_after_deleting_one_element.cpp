


/*
1493. Longest Subarray of 1's After Deleting One Element (https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24)

we only ever want to delete a 0 and never a 1 since it can never help us get a longer subarray
    keep in mind that you must delete at least one element no matter what

use a sliding window to find longest subarray 
    to get the longest subarray of only 1's after deleting a single 0
        we need to maintain a window that contains at most one 0, taking into account that we will remove that zero
        we find the largest window that contains at most one 0

algorithm:
    1. set left and right pointers for the window
    2. continue to expand the window with the right pointer while keeping track of the number of 0s in the window
    3. if the number of zeros in the window ever exceeds one, shrink the window with the left pointer until there is at most 1 zero in the window
        decrement the total number of zeros if the left pointer encounters a zero while shrinking
    4. after making sure that the window is valid, update the max size of the window with max(maxSize, r-l+1)
        r-l+1 is the size of the window with left pointer l and right pointer r

runtime: O(n) where n is the size of nums
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

int longestSubarray(vector<int>& nums) {
    int l = 0;
    int r = 0;
    int n = nums.size();
    int zeroCount = 0;

    int maxSize = 0;

    while (r < n) {
        if (nums[r] == 0) zeroCount++;

        while (zeroCount > 1) {
            if (nums[l] == 0) zeroCount--;
            l++;
        }
        maxSize = max(maxSize, r-l+1);
        r++;
    }

    return maxSize-1;
}

int main() {

    vector<int> nums = {0,1,1,1};
    cout << longestSubarray(nums) << endl;

    return 0;
}