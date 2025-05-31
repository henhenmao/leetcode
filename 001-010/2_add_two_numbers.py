
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
2. Add Two Numbers (https://leetcode.com/problems/add-two-numbers/description/)

adding numbers:
    typically when you add two numbers you would start with the ones place of both numbers 
    and work your way up as you carry the 1 when needed
    it's actually pretty convienient that the inputs and outputs are in reverse order
    since we need to start from the ones place

putting into code:
    creates a dummy ListNode to build the sum into a new linked list
    since the sizes of the two numbers could be vastly different, we have one grand total and add
    from the first number (if we can), the second number (if we can), and the carry
    keep doing this until no operations can be done

final runtime should be O(max(n, m)) where max(n, m) is the longer of the two numbers in length
space complexity of O(max(n, m)) since we need to create a new linked list of the size of max(n, m)
"""

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    res = dummy

    total = 0
    carry = 0

    while l1 or l2 or carry > 0: # keep going as long as a number still can go or a carry exists
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next 
        if l2:
            total += l2.val
            l2 = l2.next

        n = total % 10 # number that is actually put into whatever place in the result
        carry = total // 10 # get the carry the 1
        res.next = ListNode(n)
        res = res.next

    dummy = dummy.next
    return dummy