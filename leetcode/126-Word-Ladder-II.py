class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        result = []
        layer = collections.defaultdict(list)
        layer[beginWord].append([beginWord])
        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    result.extend(value for value in layer[word])
                    return result
                else:
                    for i in range(len(word)):
                        for ch in string.ascii_lowercase:
                            tmpWord = word[:i] + ch + word[i + 1:]
                            if tmpWord in wordList:
                                newLayer[tmpWord] += [wlist + [tmpWord] for wlist in layer[word]]
            wordList -= set(newLayer.keys())
            layer = newLayer

