from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # def Height(node):
        #     if not node:
        #         return 0
        #     return 1 + max(Height(node.left), Height(node.right))

        # q = deque()
        # q.append(root)
        # while q:
        #     node = q.popleft()
        #     lheight, rheight = 0, 0
        #     if node.left:
        #         q.append(node.left)
        #         lheight = Height(node.left)
        #     if node.right:
        #         q.append(node.right)
        #         rheight = Height(node.right)
        #     if abs(lheight-rheight) > 1:
        #         return False
        # return True
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return [balanced, 1+max(left[1], right[1])]
        return dfs(root)[0]