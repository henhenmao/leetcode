

#include <iostream>
#include <vector>
using namespace std;

/*
78. Subsets (https://leetcode.com/problems/subsets/)

approaching this question:
    for the first element of the list, we can split into two different possibilities:
        1. you add the element to the subset
        2. you don't add the element to the subset
    this goes for every single element in the list
    we can do this with recursive dfs and backtracking

dfs algorithm:
    1. for each element in nums, recurse without adding the current element
    2. recurse with adding the current element
    3. if you have come across all element of the list (come across, not added to subset), exit the recursion

runtime: O(2^n)
space: O(n) sub contains a max of n values
*/

void dfs(vector<int>& nums, int i, vector<int>& sub, vector<vector<int>>& res) {
    if (i >= nums.size()) {
        res.push_back(sub);
        return;
    }

    dfs(nums, i+1, sub, res);
    sub.push_back(nums[i]);
    dfs(nums, i+1, sub, res);
    sub.pop_back();
}

vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> res;
    vector<int> sub;
    dfs(nums, 0, sub, res);
    return res;
}