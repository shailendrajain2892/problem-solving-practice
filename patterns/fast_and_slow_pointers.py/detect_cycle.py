class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next :
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False    
    
Solution().hasCycle([1,2])