
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
142. Linked List Cycle II (https://leetcode.com/problems/linked-list-cycle-ii/description/?envType=problem-list-v2&envId=linked-list)

wait i spent a bit trying to solve this and i love the solution so so so much omg

assuming that there is cycle in the list, there are three important nodes we care about
    1. the head of the list
    2. the node where the cycle begins
    3. the node where a slow and fast pointer will meet given that there is a cycle

both the slow and fast pointers start at the head of the list. fast pointer will move two nodes at a time
    they will both cross the start of the cycle before they meet

let distance a = the distance between the head node and the cycle node
let distance b = the distance from the cycle node and the meet node
let distance c = the distance from the meet node and the cycle node
    distances b and c pretty much define the cycle path

when the two pointers meet, we need to notice the following
    1. the slow pointer has travelled a distance of (a + b)
        simply the distance from the head node to the meet node
    2. the fast pointer has travelled a distance of (a + b) + (c + b)
        the distance from the head node to the meet node, plus a cycle
        keep in mind that the number of laps made by the fast pointer does not matter

given that when the two pointers meet, slow pointer travels (a + b) and fast pointer travels (a + 2b + c)
    since the slow pointer travels twice as slow at the fast pointer, we can make the equation:

    2(a + b) = (a + 2b + c)
    (2a + 2b) = (a + 2b + c)    distrbute the first term
    2a = (a + c)                cancel out the 2b
    a = c                       remove a from both sides

we now know that a = c, meaning the distance from the head to the cycle start is equal to the distance from meet to cycle start
both nodes are already at the meet node
we can just move a node to the head node
    one node will now be distance a from the cycle start, and the other will be distance c from the cycle start
now just move both pointers at the same speed one step at a time until they meet
the node that they meet at will be the start of the cycle

case where there is no cycle:
    if the fast pointer reaches nullptr, no cycle

runtime: O(n) where n is the number of nodes
space: O(1)
*/

#include <iostream>
using namespace std;

ListNode *detectCycle(ListNode *head) {
    ListNode* tortoise = head;
    ListNode* hare = head;

    while (hare && hare->next) {
        tortoise = tortoise->next;
        hare = hare->next->next;

        if (tortoise == hare) {
            break;
        }
    }

    if (!hare || !hare->next) return nullptr;

    tortoise = head;
    while (tortoise != hare) {
        tortoise = tortoise->next;
        hare = hare->next;
    }

    return tortoise;
}