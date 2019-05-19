class Solution:
    def longestCommonPrefix(self, strs):
        num = len(strs)
        if num == 0:
            return ""
        sortedStr = sorted(strs)
        first = sortedStr[0]
        last = sortedStr[num - 1]
        result = ""
        numMin = min(len(first), len(last))
        for i in range(numMin):
            if first[i] == last[i]:
                result += first[i]
            else:
                return result
        return result

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
