class Solution:
    def removeKdigits(self, num, k):
        if len(num) == k: return "0"
        stack = []
        for t in num:
            while k > 0 and stack and t < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(t)
        while k > 0:
            stack.pop()
            k -= 1
        start = 0
        for i in range(len(stack) - 1): # We don't need to check last step
            if stack[i] == "0": start += 1
            else: break
        return "".join(stack[start:len(stack)])