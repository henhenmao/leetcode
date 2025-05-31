
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
19. Remove Nth Node From End of List (https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

we can "remove" a node from a linked list by changing the pointers
specifically, since the nth node is preceded by the n-1th node and followed by the n+1th node
    we can simply change the n-1th node's pointer to point to the n+1th node instead of the nth node

we just need to locate the n-1th node and change its pointer

algorithm:
    1. find the length of the list (since we are removing the nth node from the end of the list)
        we just traverse the list and count the nodes
        we now know the exact spot where we need to switch the pointer
    2. traverse the linked list again and switch the n-1th node to point to the n+1th node

runtime: O(n), where n is the length of the linked list
space: O(1)

"""



def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
    # get the length of the list
    count = head
    sz = 0
    while count:
        sz += 1
        count = count.next
    n = sz - n # change n to index from the start of the list

    if n == 0:
        return head.next # returns and removes first node

    # iterate to the nth index and change the pointer
    # of the n-1th node to the n+1th node
    # just find n-1th node and curr.next = curr.next.next
    curr = head
    for i in range(n): # iterate to the nth node
        if i+1 == n:
            curr.next = curr.next.next
            break
        curr = curr.next
    return head