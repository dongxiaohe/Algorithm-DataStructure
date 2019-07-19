class Solution(object):
    def validPalindrome(self, s):
        def isValid(t, l, r):
            while l < r:
                if t[l] != t[r]: return False
                l += 1
                r -= 1
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]: return isValid(s, left + 1, right) or isValid(s, left, right - 1)
            left += 1
            right -= 1
        return True
