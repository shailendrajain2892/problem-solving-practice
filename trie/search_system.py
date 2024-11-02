# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed. 

from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
                node.suggestions.sort()
            elif word < node.suggestions[-1]:
                node.suggestions.pop()
                node.suggestions.append(word)
                node.suggestions.sort()
    
    def get_suggestions(self, prefix):
        node = self.root
        result = []
        for char in prefix:
            if char not in node.children:
                result.extend([[]]*(len(prefix)-len(result)))
            else:
                node = node.children[char]
                result.append(node.suggestions)
        return result

t = Trie()
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
for prod in products:
    t.insert(prod)
print(t.get_suggestions(searchWord))