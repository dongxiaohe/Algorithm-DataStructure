import collections
import string
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet: return 0
        t1, t2, length = collections.deque([beginWord]), collections.deque([endWord]), 1
        """
        bidirectional bfs
        - two queue instead of one
        - only iterate smaller queue to reduce iterating huge branch
        """
        while t1 and t2:
            if len(t1) > len(t2): t1, t2 = t2, t1
            tmp = collections.deque([])
            for word in t1:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        nextWord = word[:i] + c + word[i + 1:]
                        if nextWord in t2: return length + 1
                        if nextWord in wordSet:
                            wordSet.remove(nextWord)
                            tmp.append(nextWord)
            t1 = tmp
            length += 1
        return 0
        
    def ladderLengthBFS(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        steps, queue = 0, collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            # iterate each word character looks inefficient in the first place, but the upper bound is 26.
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nextWord = word[:i] + c + word[i + 1:]
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        queue.append([nextWord, length + 1])
        return 0

    def ladderLengthSlow(self, beginWord, endWord, wordList):
        def _diff(word1, word2, diffNum):
            counter = 0
            for _, (a, b) in enumerate(zip(word1, word2)):
                if a != b and counter == diffNum: return False
                elif a != b: counter += 1
            return counter == diffNum
        wordSet = set(wordList)
        steps, queue, visited = 0, collections.deque([[beginWord, 1]]), []
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            """
            From small number of word list, the o(n) performance is better than compare string.ascii_lowercase
            However, the upper bound of this algorithm is the word list, so it may be super if collection is huge. Actually, I got TLE error in leetcode.
            """
            for each in wordSet:
                if _diff(word, each, 1):
                    queue.append([each, length + 1])
                    visited.append(each)
            for each in visited:
                if each in wordSet: wordSet.remove(each)
        return 0

print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLength("a","c",["a","b","c"]))
print(Solution().ladderLength("hot", "dog", ["hot","dog","cog","pot","dot"]))
