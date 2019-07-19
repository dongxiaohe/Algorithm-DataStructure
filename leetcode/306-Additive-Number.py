class Solution(object):
    def isAdditiveNumber(self, num):
        def isValid(num, first, second, start):
            if start == len(num): return True
            total = first + second
            return num.startswith(str(total), start) and isValid(num, second, total, start + len(str(total))) 
        n = len(num)
        if n <= 2: return False
        for i in range(1, (n >> 1) + 1):
            strFirst, j = num[:i], 1
            first = int(strFirst)
            if len(strFirst) != len(str(first)): break
            while j <= n - i - j:
                strSecond = num[i : i + j] 
                second = int(strSecond)
                if len(strSecond) != len(str(second)): break
                if isValid(num, first, second, i + j): return True
                j += 1
        return False

            
