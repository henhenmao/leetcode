
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
637. Average of Levels in Binary Tree (https://leetcode.com/problems/average-of-levels-in-binary-tree/?envType=study-plan-v2&envId=top-interview-150)

do a bfs starting on the root node of the binary tree
    queue represents the nodes at your current level
    get the length of the queue -> this is the number of nodes at the current level
    let n be the length of the queue
        pop from the queue n times and enqueue the children as usual    
    add the sum of all popped nodes
    divide by n
    rinse and repeat yap yap yap

algorithm:
    1. create a queue initialized with the root node and a result vector
    2. queue holds all nodes of the current level, get the size of the queue with int n = queue.size()
    3. create a spot in result vector where you can put the average of the level
        in this case we can just do int level = res.size() before pushing a 0 to the end
        for example, res.size() == 0 at the first iteration, and once we push a 0 to hold average, we can access res[0]
    4. pop from the queue n times so we pop every node in the current level
        for each node, add the value into res[level]
        enqueue each child in the queue if they exist
    5. after iterating through all nodes in the current level, divide res[level] by n to get the average
    6. repeat with the next level which you enqueued

runtime: O(n) where n is the number of nodes in the binary tree
space: O(n)
*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<double> averageOfLevels(TreeNode* root) {
    vector<double> res;

    queue<TreeNode*> queue;
    queue.push(root);

    while (!queue.empty()) {
        int n = queue.size();

        // creating new level in res to hold the average of the level
        int level = res.size();
        res.push_back(0);

        for (int i = 0; i < n; i++) {
            // popping from the front of thr queue
            TreeNode* curr = queue.front();
            queue.pop();

            // add the value of curr to the current sum
            res[level] += curr->val;

            // enqueue the children of curr
            if (!(curr->left == nullptr)) {
                queue.push(curr->left);
            } 
            if (!(curr->right == nullptr)) {
                queue.push(curr->right);
            }
        }
        // divide the total sum by n to get the average of the level
        res[level] *= 1.0; // convert to double (idk if this is the best way to do it)
        res[level] /= n;
    }
    return res;
}

int main() {
    return 0;

}