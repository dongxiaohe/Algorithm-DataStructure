class Solution(object):
    def isAlienSorted(self, words, order):
        orderChs = {}
        for i, c in enumerate(order): orderChs[c] = i
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if orderChs[word1[j]] > orderChs[word2[j]]: return False
                    else: break
                if j == min(len(word1), len(word2)) - 1 and len(word1) > len(word2): return False
        return True

