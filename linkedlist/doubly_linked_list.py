class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, n): 
        node = Node(n)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head # type: ignore
            self.head.prev = node # type: ignore
            self.head = node

    def traverse(self):
        tmp =self.head
        while(tmp!=None):
            print(tmp.data)
            tmp=tmp.next
        
    def delete(self):
        pass

    def search(self):
        pass


numbers = [5,2,9,7,6]
dll = DoublyLinkedList()
for n in numbers:
    dll.insert(n)
dll.traverse()