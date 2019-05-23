class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0: return matrix
        n = len(matrix[0])
        T, B, L, R, DIR, result = 0, m - 1, 0, n - 1, 0, []
        while T <= B and L <= R:
            if DIR == 0:
                for i in range(L, R + 1): result.append(matrix[T][i])
                T += 1
            elif DIR == 1:
                for i in range(T, B + 1): result.append(matrix[i][R])
                R -= 1
            elif DIR == 2:
                for i in range(R, L - 1, -1): result.append(matrix[B][i])
                B -= 1
            else:
                for i in range(B, T - 1, -1): result.append(matrix[i][L])
                L += 1
            DIR = (DIR + 1) % 4
        return result
