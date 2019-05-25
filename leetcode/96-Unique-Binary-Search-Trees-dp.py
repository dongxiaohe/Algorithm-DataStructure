class Solution:
    def numTrees(self, n):
        """
            consider G(n) is what we want
            G(n) = F(1, n) + F(2, n) + F(3, n) + ....
            F(i, n) = G(i - 1) * G(n - i)
            So this is a bottom up approach
        """
        result = [0 for _ in range(n + 1)]
        result[0] = result[1] = 1
        for i in range(2, n + 1): 
            for j in range(1, i + 1):
                result[i] += result[j - 1] * result[i - j]
        return result[n]

