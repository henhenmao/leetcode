


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


/*
24. Swap Nodes In Pairs (https://leetcode.com/problems/swap-nodes-in-pairs/description/)

algorithm:
    1. sets curr = first node, next = second node, temp = third node
    2. moves around the pointers of curr, next, and temp to swap the nodes of curr and next
    3. keep track of prev = previous node in the list to connect previous parts to new head of the swapped pair
    4. if prev is null, you are at the first pair, so update head to be at the head of linked list after first swap
    5. after pair swap, set prev = tail of the swapped pair, curr = beginning of the next pair
    6. make sure you are careful at the end of the linked list as to not set next or temp to a null value

runtime: O(n) where n is the size of the linked list
space: O(1)
*/

#include <iostream>
using namespace std;

ListNode* swapPairs(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }

    ListNode* curr = head;
    ListNode* next = head->next;
    ListNode* prev = nullptr;

    while (curr != nullptr && next != nullptr) {
        ListNode* temp = next->next;

        // perform the swap
        next->next = curr;
        curr->next = temp;

        if (prev != nullptr) {
            prev->next = next;
        } else {
            head = next;
        }

        prev = curr;

        // iterate to the next pair and check if we have made it to the end
        curr = temp;
        if (temp == nullptr) {
            next = nullptr;
        } else {
            next = temp->next;
        }
    }
    return head;
}