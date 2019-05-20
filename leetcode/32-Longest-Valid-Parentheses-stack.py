class Solution:
    def longestValidParentheses(self, s):
        stack, maxSize = [-1], 0
        for i in range(len(s)):
            if s[i] == "(": stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0: stack.append(i)
                else:  maxSize = max(maxSize, i - stack[-1])
        return maxSize
