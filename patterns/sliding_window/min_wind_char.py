from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        res, resLen = [-1, -1], float('infinity')
        l = 0
        have, need = 0, len(t)
        window = {}
        for r, char in enumerate(s):
            window[char] = 1 + window.get(char, 0)
            if char in t and window[char] == countT[char]:
                have +=1 
            
            while have == need:
                window[s[l]]-=1
                if s[l] in t and window[s[l]] < countT[s[l]]:
                    have-=1

                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                l+=1
        return s[res[0]:res[1]+1]
print(Solution().minWindow("OUZODYXAZV", "XYZ"))