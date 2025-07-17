


/*
3202. Find the Maximum Length of Valid Subsequence II (https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17)

for each subsequence of nums, make sure each instance of (nums[i] + nums[i+1]) % k are the same value
    let mod = (sub[0] + sub[1]) % 2
    keep track of the previous value added to the subsequence, let prev = previous value
    if current value (nums[i] + prev) % k != mod, cannot add nums[i] to the subsequence






*/

#include <iostream>
#include <vector>
using namespace std;

int maximumLength(vector<int>& nums, int k, int i, int prev, int mod, vector<vector<vector<int>>>& dp) {
    if (i == nums.size()) {
        return 0;
    }

    if (prev != -1 && dp[i][prev][mod] != -1) {
        return dp[i][prev][mod];
    }

    int no = maximumLength(nums, k, i+1, prev, mod, dp);

    int yes = 0;
    if (prev == -1 || (nums[i] + nums[prev]) % k == mod) {
        yes = 1 + maximumLength(nums, k, i+1, i, mod, dp);
    }

    if (prev != -1) {
        dp[i][prev][mod] = max(yes, no);
        return dp[i][prev][mod];
    } else {
        return max(yes, no);
    }
}

int maximumLength(vector<int>& nums, int k) {
    
    int n = nums.size();
    vector<vector<vector<int>>> dp(n+1, vector<vector<int>>(n+1, vector<int>(k+1, -1)));

    int res = 0;
    for (int mod = 0; mod < k; mod++) {
        res = max(res, maximumLength(nums, k, 0, -1, mod, dp));
    }
    return res;
}

int main() {

    vector<int> nums = {1,2,3,4,5};
    int k = 2;

    cout << maximumLength(nums, k) << endl;

    return 0;
}