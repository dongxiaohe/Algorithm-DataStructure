class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0: return 0 # bug free
        chMap = collections.defaultdict(int)
        i, missing, result = 0, k, 0
        for j in range(len(s)):
            chMap[s[j]] += 1
            if chMap[s[j]] == 1: missing -= 1
            while j > i and missing < 0: # bug free
                chMap[s[i]] -= 1
                if chMap[s[i]] == 0: missing += 1
                i += 1
            result = max(result, j - i + 1)
        return result

