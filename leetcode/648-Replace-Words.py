import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, strList):
        for str in strList:
            current = self.root
            for t in str:
                current = current.children[t]
            current.word = str
            
    def startWith(self, word):
        current = self.root
        for t in word:
            if current.word or current.children.get(t) is None: 
                return current.word
            current = current.children.get(t)
        return current.word

class Solution:
    def replaceWords(self, dict, sentence):
        words = sentence.split(" ")
        trie, result = Trie(), []
        trie.insert(dict)

        for word in words:
            prefix = trie.startWith(word)
            if prefix: result.append(prefix)
            else: result.append(word)
        return " ".join(result)
        
