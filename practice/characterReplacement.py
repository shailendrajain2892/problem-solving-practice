class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        for r, char in enumerate(s):
            count[char] = 1+count.get(char, 0)
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res


print(Solution().characterReplacement("AABABBA", 1))