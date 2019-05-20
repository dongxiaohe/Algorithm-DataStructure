class Solution:
    def myPow(self, x, n):
        result = 1
        absN = abs(n)
        while absN > 0:
            if absN & 1 == 1: result *= x
            absN >>= 1
            x *= x
        return result if n >= 0 else 1 / result

print(Solution().myPow(2, 9))
print(Solution().myPow(2, 2))
print(Solution().myPow(2, 3))
print(Solution().myPow(2, 5))
print(Solution().myPow(2, 7))
print(Solution().myPow(2, 10))
print(Solution().myPow(2, -9))
print(Solution().myPow(3, 9))
print(Solution().myPow(3, -9))
print(Solution().myPow(2.1, 3))
print(Solution().myPow(0.00001, 2147483647))