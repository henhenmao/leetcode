

/*
3202. Find the Maximum Length of Valid Subsequence II (https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/?envType=daily-question&envId=2025-07-17)

for each subsequence of nums, make sure each instance of (nums[i] + nums[i+1]) % k are the same value
    let mod = (sub[0] + sub[1]) % 2
    keep track of the previous value added to the subsequence, let prev = previous value
    if current value (nums[i] + prev) % k != mod, cannot add nums[i] to the subsequence

memoization state: dp[i][mod+1]
    we do mod+1 because of the mod state of -1
    basically shifting everything down by 1

algorithm:
    1. create 2d memoization table with size nums.size()+1 * k+1

    2. for each value nums[j], call recursive function with state i = j, mod = -1

    3. if mod == -1 (if first two elements haven't been chosen yet and no mod yet)
        iterate from j = i+1 to nums.size() to get each pair 
        curr_mod = (nums[i] + nums[j]) % 2 (mod for the rest of the subsequence)
        return 2 + maximumLength(nums, k, j, curr_mod, dp)
        we add 2 to the returned value since we are adding nums[i] and nums[j] to the subsequence


    4. if mod != -1 (subsequence has a mod)
        starting from j = i+1, iterate through all numbers to nums.size()
        check each value of (nums[i] + nums[j]) % 2
        only recurse into values of nums[j] where (nums[i] + nums[j]) % 2 == curr_mod
        if a valid value of j is encountered, return 1 + maximumLength(nums, k, j, curr_mod)

    5. if the previous two steps did not result in a return, return 0

    6. oh yeah and memoize everything in the dp

runtime: O(n^2 * k) where n is the size of nums
    this is because for each state of (i, mod), we loop over nums with j from i+1 to n

space: O(n * k)
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