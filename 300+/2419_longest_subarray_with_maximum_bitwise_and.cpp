


/*
2419. Longest Subarray With Maximum Bitwise AND (https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2025-07-30)

ok for this question i'm going to assume that the maximum bitwise AND of nums is equal to the maximum element in nums
    if this is not true then i do not know how to solve this problem

if the maximum bitwise AND of nums = max(nums)
    simply find the longest consecutive subarray containing only the maximum element of nums
    use a sliding window to achieve this

damn it actually works
just count the longest consecutive sequence in nums, where each element == max(nums)

runtime: O(n) where n is the length of nums
space: O(1)
*/


#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int longestSubarray(vector<int>& nums) {

    int res = 0;
    int curr = 0;
    int m = *max_element(nums.begin(), nums.end());

    for (int n : nums) {
        if (n == m) {
            curr++;
            res = max(res, curr);
        } else {
            curr = 0;
        }
    }
    return res;
}