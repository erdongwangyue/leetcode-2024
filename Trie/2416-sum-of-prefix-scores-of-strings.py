class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += 1
    def search(self, word):
        curr = self
        res = 0
        for c in word:
            res += curr.children[c].count
            curr = curr.children[c]
        return res

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        return [root.search(word) for word in words]

