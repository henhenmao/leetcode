
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
141. Linked List Cycle (https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=oizxjoit)

floyd's tortoise and hare algorithm to detect cycles in a linked list

algorithm:
    1. set a "tortoise" pointer at the beginning (slow pointer)
    2. set a "hare" pointer at the beginning (fast pointer)
    3. for every increment, move up the tortoise one node but move the hare up two nodes
    4. if a cycle ever exists, the hare will eventually lap the tortoise 
    5. if a cycle does not exist, the hare will eventually reach the end of the linked list without ever being able to lap the tortoise

runtime: O(n) where n is the size of the linked list
space: O(1)

"""

def hasCycle(head: Optional[ListNode]) -> bool:
    hare = head
    tortoise = head

    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next

        if tortoise == hare:
            return True

    return False