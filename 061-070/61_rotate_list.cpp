

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
61. Rotate List (https://leetcode.com/problems/rotate-list/description/)

when rotating a size n list k times, you can simplify rotations to be (k % n), since every n rotations goes back to the same place
now that we know that k < n after this simplification, we can split the linked list into two sections
    1. first part of the linked list that is "unaffected" by the rotation
    2. second part of the linked list that is wrapped around the beginning by the rotation
    ex. head = 1 -> 2 -> 3 -> 4, k = 2
        we can split the linked list into 1 -> 2 and 3 -> 4, since only 3 and 4 are actually getting rotated
        we simply need to move the second part in front of the first part
    
note that to swap these two sections, we only need to change two pointers
    head = 1 -> 2 -> 3 -> 4

    1. set the last node's pointer to the head node
    2. set the n-kth node's pointer to null

    edge case: if k == 0, don't do this and just return

just need to access the n-kth node and the last node, and change their pointers

runtime: O(n)
space: O(1)
*/

#include <iostream>
using namespace std;

ListNode* rotateRight(ListNode* head, int k) {
    if (k == 0 || head == nullptr || head->next == nullptr) {
        return head;
    }

    // getting length
    ListNode* curr = head;
    int n = 1;
    while (curr->next != nullptr) {
        n++;
        curr = curr->next;
    }

    curr->next = head; // make the linked list cycle

    int steps = n-(k % n)-1;
    curr = head;
    // finding the n-kth node
    for (int i = 0; i < steps; i++) {
        curr = curr->next;
    }

    ListNode* res = curr->next;
    curr->next = nullptr;

    return res;
}