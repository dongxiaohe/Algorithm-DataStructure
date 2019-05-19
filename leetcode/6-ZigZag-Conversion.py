class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        index, step = 0, 1
        result = [""] * numRows
        for x in s:
            result[index] += x 
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(result)

print(Solution().convert('PAYPALISHIRING', 3))
            
