class TrieNode:
    def __init__(self) -> None:
        self.childeren = {}
        self.endOfWord = False

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childeren:
                curr.childeren[c] = TrieNode()
            curr = curr.childeren[c]
        curr.endOfWord = True
    
    def search(self, word) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.childeren:
                return False
            curr = curr.childeren[c]
        return curr.endOfWord

    def startsWith(self, word) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.childeren:
                return False
            curr = curr.childeren[c]
        return True

t = Trie()
t.insert("apple")
print(t.search("apple"))
print(t.search("app"))
print(t.startsWith("app"))

