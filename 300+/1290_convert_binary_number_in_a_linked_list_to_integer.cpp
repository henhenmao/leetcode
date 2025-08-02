


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
1290. Convert Binary Number in a Linked List to Integer (https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/?envType=daily-question&envId=2025-07-14)

we can just iterate through the linked list, and every time we move to a new node, we multiply our current decimal value by 2
ex. 1 -> 0 -> 1
    1. add current binary value to decimal, 0 + 1 = 1
    2. move to next node
    3. multiply decimal by 2, 1 * 2 = 2
    repeat
    4. add current binary value to decimal, 2 + 0 = 2
    5. move to next node
    6. multiply decimal by 2, 2 * 2 = 4
    7. add last node value
        decimal + 1 = 5
        101 is 5 in decimal form

algorithm:  
    1. starting at the head node and decimal = 0, add the current node value to decimal (either 0 or 1)
    2. move to the next node, every time you move to a new node, double the decimal value
    3. repeat previous two steps until you reach the last node (don't double deicmal value at the end!!)

runtime: O(n) where n is the number of nodes in the linked list
space: O(1)
*/


#include <iostream>
using namespace std;

int getDecimalValue(ListNode* head) {

    int decimal = 0;

    while (head != nullptr) {
        decimal += head->val;
        decimal *= 2;
    }

    return decimal/2; // undoing the final 2x that while loop makes on the last node
}