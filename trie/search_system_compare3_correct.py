from typing import List
import bisect

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

            # Only add suggestions if we have fewer than 3
            if len(curr.suggestions) < 3:
                bisect.insort(curr.suggestions, word)
            # Ensure the suggestions do not exceed 3 and are sorted
            elif word < curr.suggestions[-1]:
                curr.suggestions.pop()  # Remove the last suggestion
                bisect.insort(curr.suggestions, word)

    def getSuggestions(self, word: str) -> List[List[str]]:
        result = []
        node = self.root

        for c in word:
            if c in node.children:
                node = node.children[c]
                result.append(node.suggestions)
            else:
                result.append([])  # No suggestions found for this prefix
                result.extend([[]] * (len(word) - len(result)))  # Fill remaining with empty lists
                break  # Stop further processing

        return result

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort products first to maintain lexicographic order in suggestions
        for prod in sorted(products):
            self.insert(prod)

        return self.getSuggestions(searchWord)
