

/*
494. Target Sum (https://leetcode.com/problems/target-sum/description/?envType=problem-list-v2&envId=dynamic-programming)

use recursive backtracking while keeping track of the current sum so far
since sums can be repeated at same indexes, have a 2d memoization table with size sum(nums) * nums.size()
    we are memoizing both positive and negative sums, so i just used two separate sum(nums) * nums.size() dp tables for positive and negative values
        i wuldn't be surprised if there were some really smart mathematical way to do this with one dp

i just realized that there is a flaw in my code where i create a dp table of sum(nums) * nums.size()
    for an input of nums = [-999, 1000], sum(nums) = 1, but the dp will need to access sum index of 1000, causing an error
        for some reason i overlooked this but leetcode still accepted the submission lmao

algorithm:
    for each element in nums at index i, you can either add nums[i] to the current total or subtract nums[i] from the current total
        memoize the recursive given the state of the current sum and the current index you are at
        if you reach the last index of nums, return whether or not your current sum equals the target

runtime: O(n * k) where n is the size of nums and k is the sum of all numbers in nums
space: O(n * k )
*/

#include <iostream>
#include <vector>
#include <numeric>
#include <cstdlib>
using namespace std;

int findTargetSumWays(vector<int>& nums, int& target, int i, int total, vector<vector<int>>& positive_dp, vector<vector<int>>& negative_dp) {
    if (i == nums.size()) {
        if (total == target) {
            return 1;
        }
        return 0;
    }

    int abs_total = abs(total);

    // check if either dp table has been memoized
    if (total < 0 && negative_dp[abs_total][i] != -1) {
        return negative_dp[abs_total][i];
    }
    if (total >= 0 && positive_dp[abs_total][i] != -1) {
        return positive_dp[abs_total][i];
    }

    // choose to add nums[i] or subtract nums[i]
    int result = 0;

    result += findTargetSumWays(nums, target, i+1, total+nums[i], positive_dp, negative_dp);
    result += findTargetSumWays(nums, target, i+1, total-nums[i], positive_dp, negative_dp);

    if (total < 0) {
        negative_dp[abs_total][i] = result;
    } else {
        positive_dp[abs_total][i] = result;
    }

    return result;
}

int findTargetSumWays(vector<int>& nums, int target) {
    int sum_nums = accumulate(nums.begin(), nums.end(), 0);

    // dp will be set as dp[current sum][index]
    // since the current sum can be negative, i'm just going to have two separate dp tables one for positive one for negative
    vector<vector<int>> positive_dp(sum_nums+1, vector<int>(nums.size()+1, -1));
    vector<vector<int>> negative_dp(sum_nums+1, vector<int>(nums.size()+1, -1));

    return findTargetSumWays(nums, target, 0, 0, positive_dp, negative_dp);

}

int main() {
    vector<int> nums = {-999, 1000};
    int target = 1;
    
    cout << findTargetSumWays(nums, target) << endl;

    return 0;
}