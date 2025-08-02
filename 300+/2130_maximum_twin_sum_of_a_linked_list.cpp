

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
2130. Maximum Twin Sum of a Linked List (https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=problem-list-v2&envId=linked-list)

basically need to be able to check each node from both ends at the same time.
we can do this using a stack

for the first half of values in the list, push all node pointers to a stack
    once the first half is traversed, the stack will contain all elements in the first half in the order from indexes n/2-1 to 0

for each element from index n/2 to n-1, just pop the top pointer from the stack and compare the sums
    keep track of the largest sum you see

algorithm:
    1. get the length of the linked list, let n = length
    2. iterate through linked list again
    3. if i < n/2, push the current pointer to a stack
    4. if i >= n/2, pop the top pointer from the stack, and get the sum of that node's value and the current node's value
    5. keep track of the maximum twin sum you see

runtime: O(n)
space: O(n)
*/

#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

int pairSum(ListNode* head) {
    stack<ListNode*> stack;

    ListNode* curr = head;
    int n = 0;
    while (curr != nullptr) {
        curr = curr->next;
        n++;
    }

    int maxSum = 0;
    curr = head;
    for (int i = 0; i < n; i++) {
        if (i < n/2) {
            stack.push(curr);
        } else {
            ListNode* twin = stack.top();
            stack.pop();
            maxSum = max(maxSum, curr->val+twin->val);
        }
        curr = curr->next;
    }
    return maxSum;
}