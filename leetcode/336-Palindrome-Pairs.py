class Solution(object):
    def palindromePairs(self, words):
        wordDict = collections.defaultdict(int)
        for i in range(len(words)):
            wordDict[words[i]] = i
        result = []
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]
                if tmp1[::-1] in wordDict and wordDict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    result.append([i, wordDict[tmp1[::-1]]])
                if j != 0 and tmp2[::-1] in wordDict and wordDict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    result.append([wordDict[tmp2[::-1]], i])
        return result
