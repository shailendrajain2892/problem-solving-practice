class Solution(object):
    def longestPalindrome(self, s:str):
        """
        :type s: str
        :rtype: str
        """
        longest_pallindrome=''
        maxLen = 1
        for i, c in enumerate(s):
            # Check for odd-length palindromes
            l, r = i, i
            new_len, new_pallindrome = self.checkPallindrome(s, l, r)
            if new_len > maxLen:
                longest_pallindrome = new_pallindrome
                maxLen = new_len

            # Check for even-length palindromes
            l, r = i, i+1
            new_len, new_pallindrome = self.checkPallindrome(s, l, r)
            if new_len > maxLen:
                longest_pallindrome = new_pallindrome
                maxLen = new_len            
        return longest_pallindrome

    def checkPallindrome(self, s:str, l:int, r:int):
        pallindrome=''
        while l>=0 and r<len(s) and s[l]==s[r]:
            r+=1
            l-=1

        # When the loop exits, l and r are one step ahead ahead so to remove those character adding 1     
        pallindrome = s[l+1:r]
        return len(pallindrome), pallindrome
print(Solution().longestPalindrome("a"))