

/*

300. Longest Increasing Subsequence (https://leetcode.com/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-interview-150)
Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

just going to do a standard recursive backtracking with dp solution that will be O(n^2) time and space

if nums[i] is strictly greater than the previous value added to the subsequence
    either choose or not choose to add nums[i] to the subsequence

memoize the index of the previously added value to the subsequence

algorithm:
    1. create a dp table of size nums.size()
    2. at each index i in the recursive call, check if nums[i] is greater than the previously added element at nums[prev_i], where 
        prev_i is the index of the previously added element in nums
        if nums[i] > nums[prev_i], you have two choices:
            1. add nums[i] to the subsequence
            2. don't add nums[i] to the subsequence
            call both recursive scenarios and return the higher value
        if nums[i] <= nums[prev_i] you only have the choice of not adding nums[i] to the subsequence
            return the recursive case where you do not add to the subsequence
    3. only one state parameter in the recursion, prev_i
        only need a 1D dp table memoizing the state of prev_i

runtime: O(n^2) where n is the size of nums
space: O(n) dp table
*/



#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int lengthOfLIS(vector<int>& nums, int i, int prev_i, vector<int>& dp) {
    if (i == nums.size()) {
        return 0;
    }

    if (dp[prev_i] != -1) {
        return dp[prev_i];
    }

    int result = 0;

    if (nums[i] > nums[prev_i]) {
        result = 1 + max(result, lengthOfLIS(nums, i+1, i, dp));
    }
    result = max(result, lengthOfLIS(nums, i+1, prev_i, dp));

    return dp[prev_i] = result;    
}

int lengthOfLIS(vector<int>& nums) {
    vector<int> dp(nums.size()+1, -1);
    int res = 0;

    for (int i = 0; i < nums.size(); i++) {
        res = max(res, 1 + lengthOfLIS(nums, i+1, i, dp));
    }

    return res;
}

int main() {

    vector<int> nums = {10,9,2,5,3,7,101,18};
    nums = {5,7,-24,12,13,2,3,12,5,6,35};

    cout << lengthOfLIS(nums) << endl;

    return 0;
}   