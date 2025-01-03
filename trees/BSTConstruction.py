class Node:
    def __init__(self, value) -> None:
        self.key = value
        self.left = None
        self.right = None

preIndex = 0
def createTreeFromInOrderAndPreOrder(inorder,preorder, startingI, endingI):
    if startingI > endingI:
        return
    global preIndex
    root = Node(preorder[preIndex])
    preIndex+=1

    for idx, i in enumerate(inorder):
        if i == root.key:
            middleI = idx
            break
    
    root.left = createTreeFromInOrderAndPreOrder(inorder, preorder, startingI, middleI-1)
    root.right = createTreeFromInOrderAndPreOrder(inorder, preorder, middleI+1, endingI)
    return root


inorder = [40,20,60,50,70,10,80,100,30]
preorder = [10,20,40,50,60,70,30,80,100]
print(createTreeFromInOrderAndPreOrder(inorder, preorder, 0, len(inorder)-1))
