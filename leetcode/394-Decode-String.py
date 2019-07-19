class Solution:
    def decodeString(self, s):
        stack, num, str = [], 0, ""
        for ch in s:
            if ch == "[":
                stack.append(str)
                stack.append(int(num))
                str = ""
                num = 0
            elif ch == "]":
                tmpNum = stack.pop()
                tmpStr = stack.pop()
                str = tmpStr + str * tmpNum
            elif ch.isdigit(): num = 10 * num + int(ch)
            else: str += ch
        return str
