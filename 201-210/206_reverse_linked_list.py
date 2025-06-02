
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
206. Reverse Linked List (https://leetcode.com/problems/reverse-linked-list/description/)

how to reverse a linked list:
    note that you just need to move the pointers around since they are linked lists

    have a variable prev that always points to the previous node
    you will work with prev, curr, and curr.next
    
    1. moving pointers:
        create a temporary pointer to the next node (temp = curr.next)
        move curr's pointer to the previous node (curr.next = prev)
    
    2. iterating to next node
        set current node to be the next "previous node" (prev = curr)
        use the temporary pointer you made earlier to move on (curr = temp)

    continue steps 1 and 2 until the end
    you are reversing every pointer until the end

runtime: O(n)
space: O(1)
"""


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None


    while curr:
        temp = curr.next

        # swap the pointer
        curr.next = prev

        # iterate to the next node
        prev = curr
        curr = temp
    
    return prev