from collections import deque
from queue import Queue
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # # Using BFS method
        # q = deque()
        # level=0
        # q.append(root)

        # while q:

        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level+=1
        # return level
    
        stack = []
        depth = 1
        stack.append([root, depth])
        res=0
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res