class Solution:
    def divide(self, dividend, divisor):
        isPositive = (dividend < 0) is (divisor < 0)
        result = 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            tmp, i = divisor, 1 
            while dividend >= tmp:
                dividend -= tmp
                result += i
                i <<= 1
                tmp <<= 1
        if not isPositive: result = -result
        return min(max(-2147483648, result), 2147483647)
print(Solution().divide(100, 2))
