class Solution:
    def titleToNumber(self, s):
        from math import pow
        lookup, count, total, square = {}, 1, 0, 0
        for i in range(65, 91):
            lookup[chr(i)] = count
            count += 1
        for i in range(len(s) - 1, -1, -1):
            total += lookup[s[i]] * int(pow(26, square))
            square += 1
        return total
