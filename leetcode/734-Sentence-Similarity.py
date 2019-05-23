class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        m, n = len(words1), len(words2)
        if m != n: return False
        pair_set = set(map(tuple, pairs))
        for i in range(m):
            if words1[i] == words2[i] or (words1[i], words2[i]) in pair_set or (words2[i], words1[i]) in pair_set: continue
            return False
        return True
