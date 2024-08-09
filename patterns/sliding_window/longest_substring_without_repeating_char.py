class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currCount=1
        maxCount=1
        if s:
            # start with two pointer pointing at 0th and 1st index
            i,j=0,1
            charList=[s[i]]
            while j < len(s):
                if s[i] != s[j] and s[j] not in charList:
                    currCount+=1
                    charList.append(s[j])
                    j+=1
                else:
                    currCount=1
                    charList.clear()
                    i=j-1
                    if s[i] == s[j]:
                        i,j=j,j+1
                    charList.append(s[i])
                # take the max value between curr Counter and maxCounter
                maxCount=max(currCount,maxCount)
            return maxCount
        else:
            return 0
print(Solution().lengthOfLongestSubstring('anviaj'))