

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/*
725. Split Linked List in Parts (https://leetcode.com/problems/split-linked-list-in-parts/?envType=problem-list-v2&envId=linked-list)

part sizes
    first know how long each part should be
        find n = length of linked list and divide n by k

    each part will have at least n // k nodes
    since parts occurring earlier should always have a size greater than or equal to the parts occuring later
        we give the leftmost n % k parts an extra node
        this ensures that parts are as equal as possible if we divide all remaining nodes among the leftmost parts

splitting into parts
    iterate over the linked list while counting how many nodes have been traversed so far
    each part needs at least n // k nodes, but also keep track how many parts have gotten an extra node
    give the first n % k parts an extra node

    when the last node of a part is reached:
        1. set a temp pointer to curr->next
        2. set curr-next = nullptr
        3. put the beginning of the part to the result vector 
            don't actually have to do it here can do it at the start since we're using pointers
        4. update curr = next

algorithm:
    1. get the length of the linked list = n
    2. let size of each part be n/k, and the number of parts with n/k + 1 nodes be n % k
    3. let extras = number of parts with n/k + 1 nodes. subtract 1 from extras every time a part is made
        if extras is greater than 0, current part gets an extra node
        let partSize be the size of the current part needed to be built
    4. add the first node of the part to the result vector
    5. iterate partSize nodes
    6. when the last node is reached, disconnect it from the rest of the linked list
    7. repeat the previous three steps until the end is reached, keep track of how many parts you have made
    8. if the end of the linked list is reached and still have not created k parts
        keep adding nullptr to the result until result.size() == k

runtime: O(n) where n is the number of nodes
space: O(1)

*/

#include <iostream>
#include <vector>
using namespace std;

vector<ListNode*> splitListToParts(ListNode* head, int k) {
    vector<ListNode*> parts;

    // finding length of list
    int n = 0;
    ListNode* curr = head;
    while (curr != nullptr) {
        n++;
        curr = curr->next;
    }

    int partSize = n/k;
    int extras = n % k;

    // cout << partSize << endl;
    // cout << extras << endl;

    // go through list and split into parts 

    ListNode* currNode = head;
    while (k > 0) {

        if (currNode == nullptr) {
            parts.push_back(nullptr);
            k--;
            continue;
        }

        int currSize = partSize-1; // including the first node of the part 
        if (extras > 0) {
            currSize++;
        }
        extras--;

        // add the first node of the part to the result vector
        parts.push_back(currNode);

        // building the current part
        while (currNode != nullptr) {
            if (currSize == 0) { // part is done
                ListNode* next = currNode->next;
                currNode->next = nullptr;
                currNode = next;
                break;
            } else {
                currNode = currNode->next;
            }
            currSize--;
        }
        k--;
    }
    return parts;
}
