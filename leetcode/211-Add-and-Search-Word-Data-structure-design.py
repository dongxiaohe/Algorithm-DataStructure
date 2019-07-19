class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.parent = TrieNode()

    def addWord(self, word):
        curr = self.parent
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word):
        def dfs(word, node):
            if not word:
                if node.isWord: self.res = True
                return
            elif word[0] == ".":
                for child in node.children:
                    dfs(word[1:], node.children[child])
            elif word[0] in node.children:
                dfs(word[1:], node.children[word[0]])
        curr = self.parent
        self.res = False
        dfs(word, curr)
        return self.res


