
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
104. Maximum Depth of Binary Tree (https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150)

use recursion to find all root to leaf paths in the binary tree
at each stage of the recursion, keep count of the current path depth from the root node
when the leaf node is reached, update the maximum path depth you have encountered so far

algorithm:
    1. if the current node has no left or right children, it is a leaf node
        update the maximum depth if the current path depth is the largest seen so far
    2. if the left child exists, add 1 to the current depth and recurse into the left child
    3. if the right child exists, add 1 to the current depth and recurse into the right child

runtime: O(n) where n is the number of nodes in the tree
space: O(n)
*/

#include <iostream>
using namespace std;

int maxDepth(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    int leftDepth = maxDepth(root->left);
    int rightDepth = maxDepth(root->right);

    return max(leftDepth, rightDepth) + 1; // adding current node to the max
}

/*
// less clean code, helper function is not actually needed

void getDepth(TreeNode* root, int count, int& maxCount) {
    if (root->right == nullptr && root->left == nullptr) {
        maxCount = max(maxCount, count);
        return;
    }
    
    if (root->left != nullptr) {
        getDepth(root->left, count+1, maxCount);
    }

    if (root->right != nullptr) {
        getDepth(root->right, count+1, maxCount);
    }
}

int maxDepth(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    int maxCount = 0;
    int count = 1;

    getDepth(root, count, maxCount);
    return maxCount;
}
*/