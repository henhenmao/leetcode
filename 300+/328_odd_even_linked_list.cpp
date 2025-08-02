
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
328. Odd Even Linked List (https://leetcode.com/problems/odd-even-linked-list/description/?envType=problem-list-v2&envId=linked-list)
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

same problem as 86. partition list but with different partitions

traverse the linked list and remove and add all odd indexed nodes to a new linked list
    all remaining nodes from the list will be even indexed lists

connect the newly formed linked list to the remaining linked list

algorithm:
    1. create dummy node and put in front of head, set prev = dummy
    2. create a new linked list to contain all odd index nodes
    3. iterate through the linked list, remove all odd index nodes and put them in the new linked list
    4. after all odd index nodes are removed, put your two linked lists together

runtime: O(n) where n is the number of nodes
space: O(1)
*/

#include <iostream>
using namespace std;

ListNode* oddEvenList(ListNode* head) {
    
    ListNode* oddHead = new ListNode();
    ListNode* evenHead = new ListNode();

    ListNode* oddTail = oddHead;
    ListNode* evenTail = evenHead;


    int i = 1;
    ListNode* curr = head;
    while (curr != nullptr) {
        ListNode* next = curr->next;

        curr->next = nullptr;

        if (i % 2 == 0) {
            evenTail->next = curr;
            evenTail = curr;
        } else {
            oddTail->next = curr;
            oddTail = curr;
        }

        curr = next;
        i++;
    }

    oddTail->next = evenHead->next;
    ListNode* res = oddHead->next;
    
    delete oddHead;
    delete evenHead;
    
    return res;
}

int main() {

    return 0;
}
