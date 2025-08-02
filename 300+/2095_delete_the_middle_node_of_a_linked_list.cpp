
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


/*
2095. Delete the Middle Node of a Linked List (https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=problem-list-v2&envId=linked-list)

get the length of the list and get the middle index
iterate through the list until you get the middle and remove it

apparently in the discussion seciton of this question the optimal solution involves a slow and fast pointer
i beat only 8% of people :(
oh well

runtime: O(n)
space: O(1)
*/

#include <iostream>
using namespace std;

ListNode* deleteMiddle(ListNode* head) {

    if (head->next == nullptr) {
        delete head; // you cannot do this
        return nullptr;
    }
    
    int n = 0;
    ListNode* curr = head;
    while (curr != nullptr) {
        n++;
        curr = curr->next;
    }

    // stop just before the middle
    curr = head;
    int mid = n/2;
    
    for (int i = 0; i < mid-1; i++) {
        curr = curr->next;
    }

    ListNode* midNode = curr->next;
    curr->next = curr->next->next;
    delete midNode;

    return head;
}