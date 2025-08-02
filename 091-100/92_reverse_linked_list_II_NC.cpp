

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
92. Reverse Linked List II (https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150)
Follow up: Could you do it in one pass?


*/




#include <iostream>
using namespace std;

ListNode* reverseBetween(ListNode* head, int left, int right) {
    
    ListNode* dummy = new ListNode();
    dummy->next = head;
    ListNode* prev = dummy;

    for (int i = 0; i < left-1; i++) {
        prev = prev->next;
    }

    ListNode* curr = prev->next;
    
    for (int i = 0; i < right-left; i++) {
        ListNode* temp = curr->next;
        curr->next = temp->next;
        temp->next = prev->next;
        prev->next = temp;
    }

    return dummy->next;
}
