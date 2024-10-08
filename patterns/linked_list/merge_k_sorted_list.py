
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self, l1, l2):
        newL = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                newL.next = ListNode(l1.val)
                l1 = l1.next
            else:
                newL.next = ListNode(l2.val)
                l2 = l2.next
            newL = newL.next
        newL.next = l1 or l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
            
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1, l2  = lists[i], lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0] 
        
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(5)

l3 = ListNode(3)
l3.next = ListNode(6)
print(Solution().mergeKLists([l1, l2, l3]))