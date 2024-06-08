import sys


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def traverse(self) -> None: 
        tmp = self.head
        while(tmp!=None):
            print(tmp.data, end=",")
            tmp=tmp.next
        print(end="\n")
        
    def insertAtEnd(self, value) -> None:
        node = Node(value)
        if self.head == None:
            # print(f"head is none now, so putting {node.data} at the beginning")
            self.head = node
        else:
            tmp = self.head
            while(tmp.next!=None):
                tmp = tmp.next
            # print(f"inserting {node.data} at the end")
            tmp.next = node # type: ignore

    def insertAtBeg(self, value) -> None: 
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head # type: ignore
            self.head = node
    
    def insertAtK(self, value, k) -> None:
        node = Node(value)
        if self.head == None:
            print('linked list empty')
        else:
            tmp = self.head
            while(tmp!=None):
                if tmp.data==k:
                    print(f"Found the key : {k} inserting new key : {node.data}")
                    node.next = tmp.next
                    tmp.next = node
                tmp=tmp.next
        
    def search(self,value) -> bool:
        if self.head == None:
            return False
        tmp = self.head
        while(tmp!=None):
            if tmp.data == value:
                print(f"found : {value}")
                return True
            tmp=tmp.next
        print(f"{value} not found")
        return False
    
    def find_n_element_from_end(self, k) -> int:
        slow=self.head
        fast=self.head
        for _ in range(k):
            fast=fast.next # type: ignore
        while(fast!=None):
            slow=slow.next # type: ignore
            fast=fast.next
        return slow.data # type: ignore
    
    def detect_loop_change_ref(self) -> bool: #approach 1
        tmp = Node(0)
        curr = self.head
        while(curr!=None and curr.next!=tmp):
            tmp2=curr.next
            curr.next=tmp # type: ignore
            curr=tmp2
        if curr==None:
            return False
        return True
    
    def detect_loop_floyd_cycle(self) -> bool:
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next # type: ignore
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    
    def reverse(self) -> None:
        curr = self.head
        prev=None
        tmp=None
        while(curr != None):
            tmp=curr.next
            curr.next=prev # type: ignore
            prev=curr
            curr=tmp
        self.head=prev


numbers = [5,8,9,12,53]
ll = LinkedList()
[ll.insertAtEnd(n) for n in numbers]
   

# ll.insertAtK(10,9)
ll.traverse()
# ll.search(1)
# k=int(sys.argv[1])
# print(f"2nd element from end = {ll.find_n_element_from_end(k)}")
print(f"Reverse a linked list")
ll.reverse()
ll.traverse()