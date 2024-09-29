class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        charSet = set()
        l, ml = 0, 0
        for char in s:
            if char not in charSet:
                charSet.add(char)
                l+=1
                res+=char
            else:
                for charS in res:
                    l-=1
                    charSet.remove(charS)
                    if charS == char:
                        break 
            ml = max(l, ml)
        return ml
    
Solution().lengthOfLongestSubstring("zxyxyz")