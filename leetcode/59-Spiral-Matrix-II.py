class Solution:
    def generateMatrix(self, n):
        matrix = [[None for _ in range(n)] for _ in range(n)]
        T, B, L, R, DIR, counter = 0, n - 1, 0, n - 1, 0, 1
        while T <= B and L <= R:
            if DIR == 0:
                for i in range(L, R + 1):
                    matrix[T][i] = counter
                    counter += 1
                T += 1
            elif DIR == 1:
                for i in range(T, B + 1):
                    matrix[i][R] = counter
                    counter += 1
                R -= 1
            elif DIR == 2:
                for i in range(R, L - 1, -1): 
                    matrix[B][i] = counter
                    counter += 1
                B -= 1
            else:
                for i in range(B, T - 1, -1): 
                    matrix[i][L] = counter
                    counter += 1
                L += 1
            DIR = (DIR + 1) % 4
        return matrix
