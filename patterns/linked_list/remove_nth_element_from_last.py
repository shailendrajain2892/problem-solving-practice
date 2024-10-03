# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        right = head
        for _ in range(n):
            right = right.next # type: ignore
        left = dummy
        while right :
            left = left.next # type: ignore
            right = right.next
        
        left.next = left.next.next # type: ignore
        return dummy.next

