class Solution:
    def findSubstring(self, s, words):
        wordsMap = collections.Counter(words)
        if not words: return []
        wordsCount, wordLen, result = len(words), len(words[0]), []
        for i in range(len(s) - wordsCount * wordLen + 1): 
            seen = collections.defaultdict(int)
            for j in range(i, i + wordsCount * wordLen, wordLen):
                currentWord = s[j: j + wordLen]
                if currentWord in wordsMap:
                    seen[currentWord] += 1
                    if seen[currentWord] > wordsMap[currentWord]: break
                else: break
            if wordsMap == seen: result.append(i)
        return result
