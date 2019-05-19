class Solution:
    def intToRoman(self, num):
        order = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
        result = ""
        while len(order) > 0:
            times = int(num / order[0][0])
            result += order[0][1] * times 
            num = num % order[0][0]
            del order[0]
        return result

print(Solution().intToRoman(3))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
print(Solution().intToRoman(2367))
