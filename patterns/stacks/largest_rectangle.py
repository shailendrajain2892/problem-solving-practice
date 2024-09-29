from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = [] # pair (idx, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxA = max(maxA, height*(i-idx))
                start = idx
            stack.append((start, h))
        for i, h in stack:
            maxA = max(maxA, h*(len(heights)-i))
        return maxA
    
print(Solution().largestRectangleArea([7, 1, 7, 2, 2, 4]))