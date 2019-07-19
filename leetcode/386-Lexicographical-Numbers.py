class Solution:
    def lexicalOrder(self, n):
        def backtrack(count, n, result):
            result.append(count)
            for i in range(10):
                tmp = 10 * count + i
                if tmp <= n: backtrack(tmp, n, result)
        result = []
        for i in range(1, 10):
            if i <= n:
                backtrack(i, n, result)
        return result
