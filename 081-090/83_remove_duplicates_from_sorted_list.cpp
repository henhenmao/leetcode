

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


/*
83. Remove Duplicates from Sorted List (https://leetcode.com/problems/remove-duplicates-from-sorted-list/?envType=problem-list-v2&envId=linked-list)

for each node, check that the next node is either null or not equal to the current node
    if this is false, remove the element

removing element reminder:
    keep track of the previous node
    to remove the current element, change pointer of previous node to point to curr->next
        don't forget to delete curr node from memory!
    
    in the case that you need to remove the first node, make a dummy node that precedes the head node so you
    have a previous node at the start

runtime: O(n) where n is the length of the list
space: O(1)
*/

ListNode* deleteDuplicates(ListNode* head) {

    ListNode* dummy = new ListNode();
    dummy->next = head;

    ListNode* curr = head;
    ListNode* prev = dummy;

    while (curr != nullptr) {
        if (curr->next != nullptr && curr->next->val == curr->val) { // remove curr
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