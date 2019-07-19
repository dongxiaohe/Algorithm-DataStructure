class TrieNode:
    def __init__(self): 
        import collections
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for t in word:
            current = current.children[t]
        current.isWord = True

    def search(self, word):
        current = self.root 
        for t in word:
            current = current.children.get(t)
            if current is None: return False
        return current.isWord

    def startsWith(self, prefix):
        current = self.root
        for t in prefix:
            current = current.children.get(t)
            if current is None: return False
        return True

