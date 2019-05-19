class Solution:
    def reverse(self, x):
        isNegative = False
        if x < 0:
           isNegative = True 
        absNum = int(str(abs(x))[::-1])
        result =  0 - absNum if isNegative else absNum
        if isNegative and result < (-1 << 31):
            return 0
        elif not isNegative and result > (1 << 31) - 1:
            return 0
        return result

print(Solution().reverse(321))
print(Solution().reverse(300))
print(Solution().reverse(-300))
print(Solution().reverse(1463847412))
