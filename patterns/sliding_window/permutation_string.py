from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1Counter = Counter(s1)
        l, r = 0, len(s1)
        while r<len(s2):
            windowCounter = Counter(s2[l:r])
            if windowCounter == s1Counter:
                return True
            l, r = l+1, r+1
        return False

print(Solution().checkInclusion('abc', "lecabee"))