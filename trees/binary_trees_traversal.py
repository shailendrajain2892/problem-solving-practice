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
        self.count=0

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
        
        root.left = self.createTreeFromInOrderAndPreOrder(inorder, preorder, startingI, middleI-1) # type: ignore
        root.right = self.createTreeFromInOrderAndPreOrder(inorder, preorder, middleI+1, endingI) # type: ignore
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
        
    def BinarySearchInsertion(self, root, key):
        if root == None:
            node = Node(key)
            return node
        if key > root.key:
            root.right = self.BinarySearchInsertion(root.right, key)
        else:
            root.left =  self.BinarySearchInsertion(root.left, key)
        return root
    
    def getSucc(self, root):
        tmp = root
        if tmp == None:
            return root
        tmp = tmp.right
        while(tmp != None and tmp.left != None):
            tmp = tmp.left
        return tmp
    
    def BinarySearchDeletion(self, root, key):
        if root == None: 
            return root
        if key > root.key:
            root.right = self.BinarySearchDeletion(root.right, key)
        elif key < root.key:
            root.left = self.BinarySearchDeletion(root.left, key)
        else:
            if root.left == None:
                temp = root.right
                del root.right
                return temp
            elif root.right == None:
                temp = root.left
                del root
                return temp
            else:
                node = self.getSucc(root)
                root.key = node.key
                root.right = self.BinarySearchDeletion(root.right, node.key)
        return root

    def kSmallElement(self, root, k, count=0):
        if root == None:
            return 
        self.kSmallElement(root.left, k, count)
        self.count+=1
        if self.count == k:
            print(root.key)
        self.kSmallElement(root.right, k, count)
    
    def kSmallElement2(self, root: Node, k: int) -> int:
        def inorder_traversal(node, k, count, result):
            if not node: 
                return count, result
            
            count, result = inorder_traversal(node.left, k, count, result)   

            #visit the node
            count+=1
            if count == k:
                result = node.key
                return count, result
            
            return inorder_traversal(node.right, k, count, result)
    
        _, result = inorder_traversal(root, k, 0, None)
        return result # type: ignore
        
    def validateBinaryTree(self, root, prev=float('-inf'), result=True):
        if not root: 
            return prev, result
        # visit left subtree
        prev, result =  self.validateBinaryTree(root.left, prev, result)

        # check parent node with prev node 
        if prev > root.key:
            result = False
            return prev, result
        else:
            prev = root.key

        # visit right subtree
        return self.validateBinaryTree(root.right, prev, result)        
    
    def validateBinaryTreeO(self, root, min_val=float('-inf'), max_val=float('inf')):
        if not root:
            return True
        
        return root.key>min_val and root.key<max_val and \
                self.validateBinaryTreeO(root.left, min_val, root.key) and \
                self.validateBinaryTreeO(root.right, root.key, max_val)
    
    def pairSum(self, root:Node, sm:int) -> bool:
        def inorder_traversal(root, sm, nodes=[], result=False):
            if not root:
                return sm, nodes, result
            
            sm, nodes, result = inorder_traversal(root.left, sm, nodes, result)

            if (sm-root.key) in nodes:
                result = True
                return sm, nodes, result
            else:
                nodes.append(root.key)
            
            return inorder_traversal(root.right, sm, nodes, result)
        _, _, result = inorder_traversal(root, sm)
        return result
    
def main():
    node = Node(12)
    node.left = Node(8) # type: ignore
    node.right = Node(16) # type: ignore
    node.left.left = Node(3) # type: ignore
    node.right.left = Node(13) # type: ignore
    node.right.right = Node(18) # type: ignore
    bt = BinaryTree()
    print(f"Pre Order Traversal: ")
    bt.PreOrderTraversal(node)
    print(bt.pre_order_trav)
    print(f"Post Order Traversal: ")
    bt.PostOrderTraversal(node)
    print(bt.post_order_trav)
    print(f"In Order Traversal:")
    # bt.InOrderTraversal(node)
    # print(bt.in_order_trav)
    bt.BFS(node)
    print(f"BFS: {bt.bfs}")
    bt.level_order_trav_by_level(node)
    print(f"Size of BST : {bt.sizeOfBST(node)}")
    print(f"Height of BST : {bt.heightOfBST(node)}")
    print(f"Max element in BST : {bt.maxElementR(node)}")
    # inorder = [40,20,60,50,70,10,80,100,30]
    # preorder = [10,20,40,50,60,70,30,80,100]
    # btTree = bt.createTreeFromInOrderAndPreOrder(inorder, preorder, 0, len(inorder)-1)
    # print(f"Binary Tree Construction: {bt.InOrderTraversal(btTree)}")
    # print(f"{bt.in_order_trav}")
    print(bt.BinarySearch(node, 13))
    # print("Adding 14 to the Binary Search Tree...")
    # root_node = bt.BinarySearchInsertion(node, 14)
    # print("Adding 7 to Binary Search Tree...")
    # root_node = bt.BinarySearchInsertion(root_node, 7)
    # root_node = bt.BinarySearchDeletion(root_node, 12)
    # bt.InOrderTraversal(root_node)
    # print(f"{bt.in_order_trav}")
    print(f" 3rd smallest element in bt : {bt.kSmallElement(node, 3)}")
    print(f"4th smallest element in bt : {bt.kSmallElement2(node, 4)}")
    _, result = bt.validateBinaryTree(node)
    print(result)
    print(f"Given Tree is binary tree : {bt.validateBinaryTreeO(node)}")
    print(f"Pair Sum exist : {bt.pairSum(node, 19)}")



main()