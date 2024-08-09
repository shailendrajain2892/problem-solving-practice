class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def InOrderTraversal(root, inorder_trav=None):
    if inorder_trav is None:
        inorder_trav = []
    if root == None:
        return inorder_trav
    InOrderTraversal(root.left, inorder_trav)
    inorder_trav.append(root.val)
    InOrderTraversal(root.right, inorder_trav)
    return inorder_trav

def PreOrderTraversal(root, preorder_trav=[]):
    if root == None:
        return preorder_trav
    
    preorder_trav.append(root.val)
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)
    return preorder_trav

def PostOrderTraversal(root, postorder_trav=[]):
    if root == None:
        return postorder_trav
    
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    postorder_trav.append(root.val)
    return postorder_trav

import queue

def BFS(root):
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    bfs_trav=[]
    while q.qsize():
        item = q.get()
        bfs_trav.append(item.val)
        if item.left:
            q.put(item.left)
        if item.right:
            q.put(item.right)
    return bfs_trav

def BFS_level_wise(root):
    print("BFS Traversal Level Wise :")
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    count=1
    while q.qsize():
        bfs_trav=[]
        count = q.qsize()
        while count:
            item = q.get()
            bfs_trav.append(item.val)
            count-=1
            if item.left:
                q.put(item.left)
            if item.right:
                q.put(item.right)
        print(bfs_trav)

def BFS_level_wise_left_element(root):
    print("BFS Traversal Level Wise Left Element :")
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    count=1
    while q.qsize():
        bfs_trav=[]
        count = q.qsize()
        while count:
            item = q.get()
            bfs_trav.append(item.val)
            count-=1
            if item.left:
                q.put(item.left)
            if item.right:
                q.put(item.right)
        print(bfs_trav[0])

def HeightOfBT(root):
    if root == None:
        return 0
    
    return 1+max(HeightOfBT(root.left), HeightOfBT(root.right))

def sizeOfBT(root):
    if root == None:
        return 0
    return 1+sizeOfBT(root.left)+sizeOfBT(root.right)

def maxElementBT(root):
    if root == None:
        return float('-inf')
    
    return max(root.val, maxElementBT(root.left), maxElementBT(root.right))

def buildTree(inorder_trav, preorder_trav):
    start, end = 0, len(preorder_trav)-1
    prefixIdx = [0]
    inorder_trav_map = {n:i for i, n in enumerate(inorder_trav)}
    return build(inorder_trav, preorder_trav, start, end, prefixIdx, inorder_trav_map)


def build(inorder_trav, preorder_trav, start, end, prefixIdx, inorder_trav_map):
    if start > end: 
        return None

    root = Node(preorder_trav[prefixIdx[0]])
    prefixIdx[0]+=1
    idx = inorder_trav_map.get(root.val)

    root.left = build(inorder_trav, preorder_trav, start, idx-1, prefixIdx, inorder_trav_map)
    root.right = build(inorder_trav, preorder_trav, idx+1, end, prefixIdx, inorder_trav_map)

    return root

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(9)
    root.right.right.right.right = Node(10)
    root.right.right.right.right.right = Node(11)
    root.left.left.left = Node(7)
    root.left.left.left.left = Node(8)
    print(f"In-Order Traversal : {InOrderTraversal(root)}")
    print(f"Pre-Order Traversal : {PreOrderTraversal(root)}")
    print(f"Post-Order Traversal : {PostOrderTraversal(root)}")

    print(f"BFS Traversal: {BFS(root=root)}")
    BFS_level_wise(root=root)
    BFS_level_wise_left_element(root=root)
    print(f"Height of BT : {HeightOfBT(root)}")
    print(f"Size of BT : {sizeOfBT(root)}")
    print(f"Max Element in BT: {maxElementBT(root)}")
    inorder_trav = [40, 20, 60, 50, 70, 10, 80, 100, 30]
    preorder_trav = [10, 20, 40, 50, 60, 70, 30, 80, 100]
    root_node = buildTree(inorder_trav, preorder_trav)
    print(InOrderTraversal(root_node, []))


main()