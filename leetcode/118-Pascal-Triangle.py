class Solution(object):
    def generate(self, numRows):
        def _pascal(arr):
            tmp = []
            for i in range(len(arr) - 1):
                tmp.append(arr[i] + arr[i + 1])
            return [1] + tmp + [1]
        result = [[1]]
        for _ in range(numRows - 1):
            result.append(_pascal(result[-1]))
        return result if numRows >= 1 else []
            
print(Solution().generate(3))

"""
1
0 1 => 1 1

1 1
0 1 1 => 1 2 1

1 2 1
0 1 2 1 => 1 3 3 1

"""