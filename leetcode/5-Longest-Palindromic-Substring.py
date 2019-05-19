class Solution:
    def longestPalindrome(self, s):
        def expandFromCenter(s, num, left, right):
            while left >= 0 and right < num and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1 # - 1 is little tricky

        start = 0
        end = 0
        num = len(s)
        for i in range(0, num):
            len1 = expandFromCenter(s, num, i, i)
            len2 = expandFromCenter(s, num, i, i + 1)
            maxLen = max(len1, len2)
            if maxLen > (end - start):
                start = i - int((maxLen - 1) / 2)  # - 1 is little tricky
                end = i + int(maxLen / 2)
        return s[start:end + 1]

print(Solution().longestPalindrome('babad'))
            
