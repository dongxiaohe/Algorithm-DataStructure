class Solution:
    def isValid(self, s):
        checker = []
        for ch in s: 
            if ch == "{":
                checker.append("}") 
            elif ch == "[":
                checker.append("]")
            elif ch == "(":
                checker.append(")")
            elif len(checker) == 0 or checker.pop() != ch:
                return False
        return len(checker) == 0
