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

    def insertAtEnd(self, value) -> None:
        node = Node(value)
        if self.head == None:
            print(f"head is none now, so putting {node.data} at the beginning")
            self.head = node
        else:
            tmp = self.head
            while(tmp.next!=None):
                tmp = tmp.next
            print(f"inserting {node.data} at the end")
            tmp.next = node

    def insertAtBeg(self, value) -> None: 
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
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
        
                
                

numbers = [5,8,9,12,53]
ll = LinkedList()
[ll.insertAtEnd(n) for n in numbers]
   

ll.insertAtK(10,9)
ll.traverse()
        