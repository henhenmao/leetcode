

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


/*
86. Parititon List (https://leetcode.com/problems/partition-list/description/?envType=problem-list-v2&envId=linked-list)

create two new linked lists starting from head1 and head2
    head1 will contain nodes less than x
    head2 will contain nodes greater than or equal to x
iterate through the linked list and move nodes less than x to head1 and the remaining to head2

once you have two separate linked lists in head1 and head2
simply connect the two by pointing the end of head1 to the beginning of head2

algorithm:
    1. create two new linked lists with dummy nodes. keep track of the heads and tails of both lists
        head1, tail1 = head and tail of linked list 1
        head2, tail2 = head and tail of linked list 2
    2. traverse through the input and move each node under x to head1 and each node greater or equal to x to head2
        let curr be the current node, and we are trying to add it to head1

        a. separate the node from the input by setting curr->next = nullptr
        b. tail1->next = curr add the curr node to the end of head1
        c. tail1 = curr to update the tail of the linked list to the newly added node
    
        after traversal, you will have two partitioned linked lists (with dummy nodes at the heads of each)
    
    3. connect the two partitioned lists while skipping the dummy nodes 
        tail1->next = head2->next

    4. return head1->next 

idk if it's good practice to delete the allocated memory to the dummy nodes or not in a leetcode problem
    i was taught to always delete memory at end of cpp program

runtime: O(n) where n is the length of the linked list
space: O(1) reusing nodes
*/


#include <iostream>
using namespace std;

ListNode* partition(ListNode* head, int x) {
    // dummy nodes
    ListNode* head1 = new ListNode(0);
    ListNode* head2 = new ListNode(0);

    ListNode* tail1 = head1;
    ListNode* tail2 = head2;

    // splitting head linked list into elements less than x and greater than or equal to x
    ListNode* curr = head;
    while (curr != nullptr) {
        ListNode* next = curr->next;

        curr->next = nullptr;

        if (curr->val < x) {
            tail1->next = curr;
            tail1 = curr;
        } else {
            tail2->next = curr;
            tail2 = curr;
        }

        curr = next;
    }
    
    tail1->next = head2->next;
    ListNode* res = head1->next;

    delete head1;
    delete head2;

    return res;
}