class Solution(object):
    def removeDuplicates(self, S):
        stack = []
        for ch in S:
            if stack and stack[-1] == ch: stack.pop()
            else: stack.append(ch)
        return "".join(stack)
