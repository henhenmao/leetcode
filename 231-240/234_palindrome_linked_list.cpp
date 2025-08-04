


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
234. Palindrome Linked List (https://leetcode.com/problems/palindrome-linked-list/description/)
Follow up: Could you do it in O(n) time and O(1) space?

easy solution would be to put all elements into a stack
    this would take O(n) space though

algorithm:
    1. put all nodes into a stack
        once stack is finished, popping from stack will give all nodes in reverse order
    2. iterate through linked list again, but pop from the stack each time and compare the two values
    3. if the two values are different, return false
    4. if iteration finishes, return true

runtime: O(n) where n is the number of nodes
space: O(n)
*/

// O(n) stack solution
#include <iostream>
#include <stack>
using namespace std;

bool isPalindrome(ListNode* head) {
    stack<ListNode*> stack;
    
    ListNode* curr = head;
    while (curr != nullptr) {
        stack.push(curr);
        curr = curr->next;
    }

    curr = head;
    while(curr != nullptr) {
        if (curr->val != stack.top()->val) {
            return false;
        }
        stack.pop();
        curr = curr->next;
    }
    return true;
}