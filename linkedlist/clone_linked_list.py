class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.random = None
        self.next = None
            
def clone_link_list(ll):
    ll_d = {}
    tmp=ll
    #create dictionary first of the existing and new ndoes
    while(tmp!=None):
        ll_d[tmp] = Node(tmp.data)
        tmp=tmp.next
    #point head to first element of the newly created node
    head = ll_d[ll]
    #crate another tmp variable to iterate 
    tmp1=ll
    #join newly crated nodes
    while(tmp1!=None):
        ll_d[tmp1].next = tmp1.next
        ll_d[tmp1].random = tmp1.random
        tmp1=tmp1.next

    return head



def printLinkedList(tmp):
    while(tmp!=None):
        print(f"Node| {tmp.data} |random |--> {tmp.random.data}")
        tmp=tmp.next
        
def main():
    n=[10,5,20,15,20]
    node = Node(10)
    node.next = Node(5)
    node.next.next = Node(20)
    node.next.next.next = Node(15)
    node.next.next.next.next = Node(20)
    
    node.random = node.next.next # random for 10->20
    node.next.random = node.next.next.next # random for 5->15
    node.next.next.random = node # random for 20->10
    node.next.next.next.random = node.next.next.next.next # random for 15-> 20
    node.next.next.next.next.random = node.next.next.next # random for 20->15

    tmp = node
    print(f"Original Linked List: ")
    printLinkedList(tmp)
    cloned_linked_list = clone_link_list(node)
    print(f"Cloned linked list: ")
    printLinkedList(cloned_linked_list)

main()
