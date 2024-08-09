# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        tmp = head
        while count != left-1:
            tmp = tmp.next
            count+=1
        leftNodePrev = tmp
        leftNode = tmp.next
        prev = leftNode
        tmp = tmp.next
        curr = tmp
        count+=2
        while count != right:
            curr = curr.next 
            tmp.next = prev
            prev = tmp
            tmp = curr
            count+=1
        leftNodePrev.next = tmp