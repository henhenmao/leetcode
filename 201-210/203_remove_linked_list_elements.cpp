



// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};



/*
203. Remove Linked List Elements (https://leetcode.com/problems/remove-linked-list-elements/?envType=problem-list-v2&envId=linked-list)

removing element:
    keep track of the previous node
    to remove the current element, change pointer of previous node to point to curr->next
        don't forget to delete curr node from memory!
    
    in the case that you need to remove the first node, make a dummy node that precedes the head node so you
    have a previous node at the start

runtime: O(n) where n is the number of nodes
space: O(1)
*/

#include <iostream>
using namespace std;

ListNode* removeElements(ListNode* head, int val) {
    ListNode* dummy = new ListNode();
    dummy->next = head;

    ListNode* curr = head;
    ListNode* prev = dummy;

    while (curr != nullptr) {
        if (curr->val == val) {
            prev->next = curr->next;
            delete curr;
            curr = prev->next;
        } else {
            prev = curr;
            curr = curr->next;
        }
    }

    ListNode* res = dummy->next;
    delete dummy;
    return res; 
}