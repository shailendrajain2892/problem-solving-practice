class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        stack = []
        res = [0]*len(temperatures)
        for tIdx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                val = stack.pop()
                _, idx = val
                res[idx] = tIdx - idx
            stack.append((t,tIdx))
        return res

temp = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures=temp))