


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


/*
113. Path Sum II (https://leetcode.com/problems/path-sum-ii/description/)

same thing as path sum I but keep track of a list of all path sums instead of returning true at the first encounter
during the dfs, need to keep track of both the sum and the current path of values

algorithm:
    1. base case: if node is null, return
    2. check if the current node is a leaf node (both children are null)
    3. if current node is a leaf node, chcek if the current sum is equal ot the target sum
    4. if current sum equals target sum, add the current path into the result
    5. continue the dfs into children
        add current value into the path to continue building on path
        add the current value into the current sum to continue building the sum
    6. return the result vector in the end
    
runtime: O(n) where n is the size of the tree
space: O(n)
*/

#include <iostream>
#include <vector>
using namespace std;

void dfs(vector<vector<int>>& res, TreeNode* root, int currSum, int& targetSum, vector<int>& path) {

    if (!root) {
        return;
    }

    currSum += root->val;
    path.push_back(root->val);

    // backtrack if the current sum goes over the target

    // when leaf node is found, check if the path is equal to target and add to res if true
    if (!root->left && !root->right) {
        if (currSum == targetSum) {
            res.push_back(path);
        }
    }

    // recusion (check left and right individually)
    if (root->left) {
        dfs(res, root->left, currSum, targetSum, path);
    }

    if (root->right) {
        dfs(res, root->right, currSum, targetSum, path);
    }

    path.pop_back();
}

vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
    vector<vector<int>> res;
    vector<int> path;
    dfs(res, root, 0, targetSum, path);
    return res;        
}