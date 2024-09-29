from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carFleet = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(carFleet)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and  stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

poisition = [4,1,0,7]
speed = [2,2,1,1]
print(Solution().carFleet(10, poisition, speed))