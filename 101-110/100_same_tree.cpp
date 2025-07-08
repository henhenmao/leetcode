
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
100. Same Tree (https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150)

this problem is very simple if you realize that you can just do a regular dfs recursive call
but on both trees at the same time

algorithm:
    1. if both nodes you are looking at for each tree is null, return true as everything is fine
    2. if the first case didn't pass, at least one tree is not null, so if a node is null, return false
    3. recursively call the previous two steps on the left child of both trees 
    4. call the steps on the right child of both trees twoo

runtime: O(n) where n is the minimum size of the two trees
space: O(n)
*/

bool isSameTree(TreeNode* p, TreeNode* q) {
    if (p == nullptr && q == nullptr) {
        return true;
    }
    if (p == nullptr || q == nullptr) {
        return false;
    }
    return (p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
}