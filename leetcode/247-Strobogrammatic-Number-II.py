class Solution(object):
    def findStrobogrammatic(self, n):
        def helper(n, m):
            if n == 0: return [""]
            if n == 1: return ["0", "1", "8"]
            result = []
            strlist = helper(n - 2, m)
            for s in strlist:
                if n != m: result.append("0" + s + "0")
                result.append("1" + s + "1")
                result.append("6" + s + "9")
                result.append("8" + s + "8")
                result.append("9" + s + "6")
            return result
        return helper(n, n)
