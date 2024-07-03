from queue import Queue


class Node:
    def __init__(self, value) -> None:
        self.key = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.pre_order_trav = []
        self.post_order_trav = []
        self.in_order_trav = []
        self.bfs = []
        self.preindex = 0

    def PreOrderTraversal(self, node):
        if node == None:
            return
        self.pre_order_trav.append(node.key)
        self.PreOrderTraversal(node.left)
        self.PreOrderTraversal(node.right)

    def InOrderTraversal(self, node):
        if node == None:
            return
        self.InOrderTraversal(node.left)
        self.in_order_trav.append(node.key)
        self.InOrderTraversal(node.right)

    def PostOrderTraversal(self, node):
        if node == None:
            return
        self.PostOrderTraversal(node.left)
        self.PostOrderTraversal(node.right)
        self.post_order_trav.append(node.key)

    def BFS(self, node):
        if node == None:
            return
        bfsQueue = Queue()
        bfsQueue.put(node)
        while(bfsQueue.qsize() != 0):
            node = bfsQueue.get()
            self.bfs.append(node.key)
            if node.left!=None:
                bfsQueue.put(node.left)
            if node.right!=None:
                bfsQueue.put(node.right)
            
    def level_order_trav_by_level(self,root):
       
        if root == None:
            return
        bfsQueue = Queue()
        bfsQueue.put(root)
        while(True):
            levels = []
            nodeCount = bfsQueue.qsize()
            if nodeCount == 0:
                break    
            while(nodeCount>0):
                node = bfsQueue.get()
                print(node.key, end="\t")
                if node.left!=None:
                    bfsQueue.put(node.left)
                if node.right!=None:
                    bfsQueue.put(node.right)    
                nodeCount-=1   
            print("\n")


    def leftview(self, root):
        pass

    def sizeOfBST(self, root):
        if root == None:
            return 0
        return 1 + self.sizeOfBST(root.left) + self.sizeOfBST(root.right)

    def heightOfBST(self,root):
        if root == None: 
            return 0
        return 1 + max(self.heightOfBST(root.left), self.heightOfBST(root.right))
    
    # max Element using BFS
    def maxElementB(self, root): 
        maxE = float("-inf")
        q = Queue()
        q.put(root)
        while q.qsize() != 0:
            node = q.get()
            key = node.key
            if key > maxE:
                maxE = key
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return maxE
    
    def maxElementR(self,root):
        if root == None:
            return 0
        return max(root.key, self.maxElementR(root.left), self.maxElementR(root.right))
    
    def createTreeFromInOrderAndPreOrder(self, inorder,preorder, startingI, endingI):
        if startingI > endingI:
            return
        root = Node(preorder[self.preindex])
        self.preindex+=1

        for idx, i in enumerate(inorder):
            if i == root.key:
                middleI = idx
                break
        
        root.left = self.createTreeFromInOrderAndPreOrder(inorder, preorder, startingI, middleI-1)
        root.right = self.createTreeFromInOrderAndPreOrder(inorder, preorder, middleI+1, endingI)
        return root
    
    def BinarySearch(self, root, key):
        if root == None:
            return False
        if root.key == key:
            return True
        if key > root.key:
            return self.BinarySearch(root.right, key)
        else:
            return self.BinarySearch(root.left, key)
def main():
    node = Node(12)
    node.left = Node(8)
    node.right = Node(16)
    node.left.left = Node(3)
    node.right.left = Node(13)
    node.right.right = Node(18)
    bt = BinaryTree()
    print(f"Pre Order Traversal: ")
    bt.PreOrderTraversal(node)
    print(bt.pre_order_trav)
    print(f"Post Order Traversal: ")
    bt.PostOrderTraversal(node)
    print(bt.post_order_trav)
    print(f"In Order Traversal:")
    bt.InOrderTraversal(node)
    print(bt.in_order_trav)
    bt.BFS(node)
    print(f"BFS: {bt.bfs}")
    bt.level_order_trav_by_level(node)
    print(f"Size of BST : {bt.sizeOfBST(node)}")
    print(f"Height of BST : {bt.heightOfBST(node)}")
    print(f"Max element in BST : {bt.maxElementR(node)}")
    inorder = [40,20,60,50,70,10,80,100,30]
    preorder = [10,20,40,50,60,70,30,80,100]
    btTree = bt.createTreeFromInOrderAndPreOrder(inorder, preorder, 0, len(inorder)-1)
    print(f"Binary Tree Construction: {bt.InOrderTraversal(btTree)}")
    print(f"{bt.in_order_trav}")
    print(bt.BinarySearch(node, 13))

main()