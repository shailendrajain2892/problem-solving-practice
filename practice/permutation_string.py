from collections import Counter
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Counter = Counter(s1)
        s2Counter = Counter(s2[:len(s1)])
        
        if s1Counter == s2Counter:
            return True
        l = 0
        for i in range(len(s1), len(s2)):
            s2Counter[s2[i]]+=1
            if s2Counter[s2[l]] == 1:
                del s2Counter[s2[l]]
            else:
                s2Counter[s2[l]]-=1
            l+=1

            if s2Counter == s1Counter: 
                return True
        return False
    
s1 = "abc"
s2 = "lecaabee"
print(Solution().checkInclusion(s1, s2))