

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
1721. Swapping Nodes in a Linked List (https://leetcode.com/problems/swapping-nodes-in-a-linked-list/?envType=problem-list-v2&envId=linked-list)

only need to swap the values not the node themselves which makes this question mad easy
traverse through the linked list, put pointers at the two nodes at positions k and n-k
swap the values i guess

runtime: O(n) where n is the number of nodes
space: O(1)
*/


#include <iostream>
#include <algorithm>
using namespace std;

ListNode* swapNodes(ListNode* head, int k) {
    if (head->next == nullptr) {
        return head;
    }

    // getting n
    ListNode* curr = head;
    int n = 0;
    while (curr != nullptr) {
        n++;
        curr = curr->next;
    }

    int left = k-1;
    int right = n-k;

    ListNode* leftNode = head;
    ListNode* rightNode = head;

    for (int i = 0; i < left; i++) {
        leftNode = leftNode->next;
    }
    for (int i = 0; i < right; i++) {
        rightNode = rightNode->next;
    }

    swap(leftNode->val, rightNode->val);
    return head;      
}