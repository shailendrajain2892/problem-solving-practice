class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def BSTSearch(root:Node, key:int) -> bool:
    if root == None:
        return False
    if root.val == key:
        return True
    if key > root.val:
        return BSTSearch(root.right, key)
    else:
        return BSTSearch(root.left, key)

def insert(root:Node, valToBeInserted:int) -> Node:
    if root == None:
        return Node(valToBeInserted)
    if valToBeInserted > root.val:
        root.right = insert(root.right, valToBeInserted)
    else:
        root.left = insert(root.left, valToBeInserted)
    return root

def findInOrderSucc(root):
    curr = root.right
    while curr and curr.left:
        curr = curr.left
    return curr

def delNode(root:Node, valToBeDeleted:int) -> Node:
    if root == None:
        return
    if valToBeDeleted > root.val:
        root.right = delNode(root.right, valToBeDeleted)
    elif valToBeDeleted < root.val:
        root.left = delNode(root.left, valToBeDeleted)
    else:
        if root.left == None:
            tmp = root.right
            del root
            return tmp
        elif root.right == None:
            tmp = root.left
            del root
            return tmp
        else:
            succ = findInOrderSucc(root)
            root.val = succ.val
            root.right = delNode(root.right, succ.val)
    return root

def inOrderTraversal(root:Node, inorder_trav:list[int]=None) -> list[int]:
    if inorder_trav is None:
        inorder_trav=[]
    if root is None:
        return inorder_trav
    inOrderTraversal(root.left, inorder_trav)
    inorder_trav.append(root.val)
    inOrderTraversal(root.right, inorder_trav)
    return inorder_trav

def kthSmallestElement(root:Node, k):
    count=[0]
    result=[None]
    def inOrder_Traversal(root:Node, k:int, count:list, result:list) -> None:
        if root is None:
            return 
        if result[0] is not None:
            return
        inOrder_Traversal(root.left, k, count, result)
        count[0]+=1
        if count[0] == k:
            result[0] = root.val
            return 
        inOrder_Traversal(root.right, k, count, result)

    inOrder_Traversal(root, k, count, result)
    return result[0]

def checkBST(root, prev=[float('-inf')]):
    if root == None:
        return True
    
    if not checkBST(root.left, prev):
        return False
    
    if root.val < prev[0]:
        return False
    
    prev[0] = root.val
    return checkBST(root.right, prev)


def checkBSTRange(root, min_val=float('-inf'), max_val=float('inf')):
    if root == None:
        return True
    
    return root.val > min_val and root.val < max_val and \
            checkBSTRange(root.left, min_val, root.val) and \
            checkBSTRange(root.right, root.val, max_val)

def pairSum(root, targetSum, diffList = None) -> bool:
    
    if diffList is None:
        diffList = []
    
    if root is None:
        return False
    
    if pairSum(root.left, targetSum, diffList):
        return True

    diff = targetSum - root.val
    if diff in diffList:
        return True
    else:
        diffList.append(root.val)
    
    return pairSum(root.right, targetSum, diffList)


def binaryTreePaths( root):
    def dfs(node, path, paths):
        if node:
            # Add the current node's value to the path
            path += str(node.val)
            
            # If it's a leaf, add the path to the list of paths
            if not node.left and not node.right:
                paths.append(path)
            else:
                # Continue the path with '->' and explore left and right children
                path += "->"
                dfs(node.left, path, paths)
                dfs(node.right, path, paths)

    paths = []
    dfs(root, "", paths)
    return paths

def BinaryTreePathMaxSum(root):

    maxPathSum = float('-inf')
    def dfs(root):
        nonlocal maxPathSum
        if not root:
            return 0
        leftMax = max(dfs(root.left), 0)
        rightMax = max(dfs(root.right), 0)

        maxPathSum = max(maxPathSum, root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)

    dfs(root)
    return maxPathSum

def main():
    root = Node(15)
    root.left = Node(5)
    root.left.left = Node(3)

    root.right = Node(20)
    root.right.left = Node(18)
    root.right.left.left = Node(16)

    #         15
    #        /  \
    #       5   20
    #      /    /
    #     3    18
    #          / \
    #         16  19
    val = 16
    print(f"Search {val} in BST: {BSTSearch(root, val)}")
    print(f"InOrder Traversal of BST: {inOrderTraversal(root)}")
    val = 19
    print(f"Inserting {val} in BST: {insert(root, val)}")
    print(f"InOrder Traversal of BST: {inOrderTraversal(root)}")
    val = [18,5,19]
    # for v in val:
    #     print(f"Deleting {v} in BST: {delNode(root, v)}")
    #     print(f"InOrder Traversal of BST: {inOrderTraversal(root)}")
    k=2
    print(f"{k}nd small elment in BST : {kthSmallestElement(root, 2)}")
    print(f"Check BST : {checkBST(Node(5))}")
    print(f"Check BST Range : {checkBSTRange(Node(6))}")
    print(f"Pair Sum Exist : {pairSum(root, 10)}")
    print(f"Binary Tree Path : {binaryTreePaths(root)}")
    print(f"Binary Tree Path Sum: {BinaryTreePathMaxSum(root)}")

main()