# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMapping = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            nodeMapping[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = nodeMapping[curr]
            copy.next = nodeMapping[curr.next]
            copy.random = nodeMapping[curr.random]
            curr = curr.next
        return nodeMapping[head]



head = Node(3)
head.next = Node(7)
head.next.next = Node(4)
head.next.next.next = Node(5)
# start assigning random pointer
head.next.random = head.next.next.next
head.next.next.random = head.next
head.next.next.next.random = head
newLinkedList = Solution().copyRandomList(head)
print(head)
print(newLinkedList)
while newLinkedList:
    print(f"val : {newLinkedList.val}")
    if newLinkedList.random:
        print(f"random val : {newLinkedList.random.val}")
    newLinkedList = newLinkedList.next