class Solution(object):
    def getRow(self, rowIndex):
        result = [1]
        for _ in range(rowIndex):
            result = [x + y for x, y in zip([0] + result, result + [0])]
        return result

"""
1 1
0 1 1
1 1 0 => 1 2 1 

"""