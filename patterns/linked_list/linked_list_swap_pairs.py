# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        if head and head.next:
            curr = head
            next = curr.next
            prev = dummyNode
            head = next
            while curr and next:
                # update next pointer
                curr.next = curr.next.next
                next.next = curr
                prev.next = next
                # move pointers
                prev = curr
                curr = curr.next
                next = curr.next if curr else None
                
        
        return dummyNode.next
