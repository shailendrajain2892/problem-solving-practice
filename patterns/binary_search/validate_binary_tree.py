class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')  # Keeps track of the previous node value in in-order traversal
        
        def inOrderValidate(node):
            nonlocal prev
            if not node:
                return True
            
            # Traverse the left subtree
            if not inOrderValidate(node.left):
                return False
            
            # Check the current node value
            if node.val <= prev:
                return False
            prev = node.val  # Update previous value
            
            # Traverse the right subtree
            return inOrderValidate(node.right)
        
        return inOrderValidate(root)
    
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def inOrderTrave(root, res=None):
#             if not root:
#                 return res
#             if not res:
#                 res = []
#             res = inOrderTrave(root.left, res)
#             res.append(root.val)
#             res = inOrderTrave(root.right, res)
#             return res
#         res = inOrderTrave(root)
#         print(res)
#         prev = float('-inf')
#         for n in res:
#             if n <= prev:
#                 return False
#             prev = n
#         return True