class Solution(object):
    def wordPatternMatch(self, pattern, str):
        def backtrack(pattern, str, i, j, patternMap, seen): # the key
            if i == len(pattern) and j == len(str): return True
            if i == len(pattern) or j == len(str): return False
            ch = pattern[i]
            if ch in patternMap:
                if not str.startswith(patternMap[ch], j): return False
                return backtrack(pattern, str, i + 1, j + len(patternMap[ch]), patternMap, seen)
            for k in range(j, len(str)):
                strSection = str[j: k + 1]
                if strSection in seen: continue
                patternMap[pattern[i]] = strSection
                seen.add(strSection)
                if backtrack(pattern, str, i + 1, k + 1, patternMap, seen): return True
                patternMap.pop(pattern[i])
                seen.remove(strSection)
            return False
        patternMap, seen = {}, set()
        return backtrack(pattern, str, 0, 0, patternMap, seen)

