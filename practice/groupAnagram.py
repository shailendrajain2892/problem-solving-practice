from collections import defaultdict
from typing import List


class Solution:
    def list_to_unique_number(self, lst):
        # Determine the base
        base = max(lst) + 1
        
        # Compute the unique number
        unique_number = 0
        for digit in lst:
            unique_number = unique_number * base + digit
        
        return unique_number
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagGroup = defaultdict(list)
        charA = [0]*26
        for word in strs:
            wCharA = charA.copy()
            for char in word:
                wCharA[ord(char)-ord('a')]+=1
            key  = self.list_to_unique_number(wCharA)
            anagGroup[key].append(word)
        return [wordList for wordList in anagGroup.values()]
strs = ["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]
print(Solution().groupAnagrams(strs))