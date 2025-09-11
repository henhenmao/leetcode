
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
437. Path Sum III (https://leetcode.com/problems/path-sum-iii/)



*/


#include <iostream>
#include <vector>
using namespace std;

int countPaths(TreeNode* root, int curr, int targetSum) {
    if (!root) return 0;
    if (curr == targetSum) return 1;

    int total = 0;

    total += countPaths(root->left, curr+root->val, targetSum);
    total += countPaths(root->right, curr+root->val, targetSum);

    total += countPaths(root->left, root->val, targetSum);
    total += countPaths(root->right, root->val, targetSum);

    return total;

}



int pathSum(TreeNode* root, int targetSum) {

    vector<int> path;

    int res = 0;
    res += countPaths(root, 0, targetSum);
    return res;
}