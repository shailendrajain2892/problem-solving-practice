from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        counterT = Counter(t)

        window = defaultdict(int)

        have, need = 0, len(counterT)
        l = 0
        res, resLen = [-1, -1], float('inf')
        for r in range(len(s)):
            window[s[r]]+=1

            if s[r] in counterT and window[s[r]] == counterT[s[r]]:
                have+=1
            
            while have == need:
                if resLen >= (r-l+1):
                    res = [l, r]
                    resLen = r-l+1
                window[s[l]]-=1
                if s[l] in counterT and window[s[l]] < counterT[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if resLen != float('inf') else ""

s="ADOBECODEBANC"
t="ABC"
print(Solution().minWindow(s, t))