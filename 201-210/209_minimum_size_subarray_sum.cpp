

/*
209. Minimum Size Subarray Sum (https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150)
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

sliding window algorithm:
    start with left and right pointers at start of nums
    increment right pointer to expand the window while keeping track of the sum of the window
    while sum is greater than or equal to target, increment left pointer to shrink the window
        every time left pointer is shifted update the minimum size of the window seen so far

runtime: O(n) where n is size of nums
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

int minSubArrayLen(int target, vector<int>& nums) {
    int n = nums.size();
    int left = 0, right = 0;
    int minSize = INT_MAX;
    int currSum = 0;

    while (right < n) {

        currSum += nums[right];

        while (currSum >= target) {
            // cout << "indices: " << left << " " << right << endl;
            minSize = min(minSize, right-left+1);
            currSum -= nums[left];
            left++;
        }

        right++;
    }

    return minSize != INT_MAX ? minSize : 0;
}

int main() {
    vector<int> nums = {2,3,1,2,4,3};
    int target = 7;

    cout << minSubArrayLen(target, nums) << endl;

    return 0;
}

