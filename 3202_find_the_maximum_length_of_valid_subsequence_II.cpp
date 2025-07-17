


/*
3202. Find the Maximum Length of Valid Subsequence II (https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17)

for each subsequence of nums, make sure each instance of (nums[i] + nums[i+1]) % k are the same value
    let mod = (sub[0] + sub[1]) % 2
    keep track of the previous value added to the subsequence, let prev = previous value
    if current value (nums[i] + prev) % k != mod, cannot add nums[i] to the subsequence

memoization state:




*/

#include <iostream>
#include <vector>
using namespace std;

int maximumLength(vector<int>& nums, int k, int i, int mod, vector<vector<int>>& dp) {
    if (i == nums.size()) {
        return 0;
    }

    if (dp[i][mod+1] != -1) {
        return dp[i][mod+1];
    }

    int yes = 0;
    if (mod == -1) { // first subsequence element
        for (int j = i+1; j < nums.size(); j++) {
            // setting the current modulo of (sub[0] + sub[1]) % k
            int curr_mod = (nums[i] + nums[j]) % k;
            yes = max(yes, 2 + maximumLength(nums, k, j, curr_mod, dp));
        }
        dp[i][mod+1] = yes;
        return dp[i][mod+1];
    }

    for (int j = i+1; j < nums.size(); j++) {
        // check that adding the next element will be valid
        int curr_mod = (nums[i] + nums[j]) % k;
        if (curr_mod == mod) {
            dp[i][mod+1] = 1 + maximumLength(nums, k, j, mod, dp);
            return dp[i][mod+1];
        }
    }

    dp[i][mod+1] = 0;
    return 0;   
}

int maximumLength(vector<int>& nums, int k) {
    
    int n = nums.size();
    vector<vector<int>> dp(nums.size()+1, vector<int>(k+1, -1)); // dp[i][mod   ]

    int res = 0;
    for (int i = 0; i < nums.size(); i++) {
        res = max(res, maximumLength(nums, k, i, -1, dp));
    }
    return res;
}

int main() {

    vector<int> nums = {1,2,3,4,5};
    int k = 2;

    cout << maximumLength(nums, k) << endl;

    return 0;
}