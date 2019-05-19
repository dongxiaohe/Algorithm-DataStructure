class Solution:
    def romanToInt(self, s):
        twoCharacterMatch = [[900, 'CM'], [400, 'CD'], [90, 'XC'], [40, 'XL'], [9, 'IX'],  [4, 'IV']]
        oneCharacterMatch = [[1000, 'M'], [500, 'D'], [100, 'C'],  [50, 'L'], [10, 'X'],  [5, 'V'], [1, 'I']]
        num = len(s)
        result = 0
        while num > 0:
            tmp = next(filter(lambda x: num >= 2 and x[1] == s[0:2], twoCharacterMatch), None)
            if tmp:
                result += tmp[0]
                s = s[2:]
                num -= 2
            else: 
                tmp = next(filter(lambda x: x[1] == s[0], oneCharacterMatch))
                result += tmp[0]
                s = s[1:]
                num -= 1
        return result
print(Solution().romanToInt('MCMXCIV'))
