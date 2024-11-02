# Design Word Search Data Structure
# Design a data structure that supports adding new words and searching for existing words.

# Implement the WordDictionary class:

# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

class TrieNode:
    def __init__(self):
        self.childeren = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.childeren:
                curr.childeren[char] = TrieNode()
            curr = curr.childeren[char]
        curr.endOfWord = True

    def search(self, word):
        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                char = word[j]
                if char == ".":
                    for child in curr.childeren.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if char not in curr.childeren:
                        return False
                    curr = curr.childeren[char]
            return curr.endOfWord
        return dfs(0, self.root)

wd = WordDictionary()
wd.insert("mad")
wd.insert("bad")
wd.insert("sad")
# print(f" search pad : {wd.search("pad")}")
# print(f"search .ad : {wd.search(".ad")}")
# print(f"seaarch mad: {wd.search("mad")}")
print(f"seaarch mad: {wd.search("m..")}")