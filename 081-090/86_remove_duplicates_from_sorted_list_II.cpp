


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
86. Remove Duplicates From Sorted List II (https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=problem-list-v2&envId=linked-list)

for each curr node, keep track of the previous node and the next node
    check if curr->val == next->val
    if true, that is a duplicate
        need to rewire the previous node pointer to point to the first node that isn't equal ot curr->val (or nullptr)
            if nullptr is reached, return
        once pointer is changed, set prev to the current node and move curr up

    if false, increment prev and curr

algorithm:
    1. create a dummy node at the start incase we need to remove the first element
    2. set prev = dummy and curr = head
    3. we want to always keep track of prev, curr, and next nodes, only continue if curr and next are not nullptrs
    4. if curr and next nodes have the same value, we have found a duplicate
        we want to continue to iterate curr forward until curr->val != next->val
            stop iteration if curr reaches the end of list
        do not update next so we can keep comparing curr->val to next->val
            do not update prev too
    5. once curr->val != next->val, curr has now skipped through all duplicates
        point prev->next to curr to remove all duplicates

runtime: O(n) where n is the number of nodes
space: O(1)
*/

#include <iostream>
using namespace std;

ListNode* deleteDuplicates(ListNode* head) {
    ListNode* dummy = new ListNode();
    dummy->next = head;

    ListNode* curr = head;
    ListNode* prev = dummy;

    while (curr && curr->next) {
        ListNode* next = curr->next;
        if (curr->val == next->val) {
            while (curr != nullptr && curr->val == next->val) {
                curr = curr->next;
            }
            prev->next = curr;
        } else {
            prev = curr;
            curr = curr->next;
        }    
    }

    ListNode* res = dummy->next;
    delete dummy;
    return res;
}