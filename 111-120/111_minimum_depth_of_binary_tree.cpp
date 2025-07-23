
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
111. Minimum Depth of Binary Tree (https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)

run through the binary tree with a breadth first search
first leaf node encountered is the closest leaf node to the root node

algorithm:
    1. initialize a queue containing pairs of TreeNode and path length
        add the {root node, 1} as the first value of the queue
        make sure to check that the root node isn't null in the first place
    2. while the queue is not empty, pop the head of the queue
        if the node in the head of the queue is a leaf node, immediately return the associated path length
    3. add the left child and right child to the queue and add 1 to each of their path lengths

runtime: O(n) where n is the number of nodes in the tree
space: O(n)
*/

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int minDepth(TreeNode* root) {
    if (!root) {
        return 0;
    }

    queue<pair<TreeNode*, int>> queue;
    queue.push({root, 1});

    pair<TreeNode*, int> curr;
    while (!queue.empty()) {
        curr = queue.front();
        queue.pop();
        TreeNode* node = curr.first;
        int path = curr.second;

        if (node->left == nullptr && node->right == nullptr) {
            return path;
        }

        if (node->left) {
            queue.push({node->left, path+1});
        }
        if (node->right) {
            queue.push({node->right, path+1});
        }
    }
    return -1;
}