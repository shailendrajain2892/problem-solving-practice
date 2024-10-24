
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def deserialize(data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        i = 0
        def dfs():
            nonlocal i
            if values[i] == "N":
                i+=1
                return None

            root = TreeNode(int(values[i]))
            i+=1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

tree_string = "1,2,N,N,3,4,N,N,5,N,N"
deserialize(tree_string)