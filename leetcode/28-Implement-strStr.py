class Solution:
    def strStr(self, haystack, needle):
        nFind = len(needle)
        if nFind == 0: return 0
        n = len(haystack)
        if n == 0: return -1
        for i in range(n):
            if haystack[i : i + nFind] == needle:
                return i
        return -1    
