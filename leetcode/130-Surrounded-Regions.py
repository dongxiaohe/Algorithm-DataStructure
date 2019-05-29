class Solution:
    def solve(self, board):
        if not board: return
        def _bfsUpdateToOne(i, j, board, m, n):
            queue = [(i, j)]
            while queue:
                a, b = queue.pop(0)
                if 0 <= a and a < m and 0 <= b and b < n:
                    if board[a][b] == REPLACE:
                        board[a][b] = '1'
                        queue.extend([(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)])
        m, n, REPLACE = len(board), len(board[0]), 'O'
        for i in range(m):
            for j in range(n): 
                if board[i][j] == REPLACE and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    _bfsUpdateToOne(i, j, board, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == REPLACE: board[i][j] = 'X'
                elif board[i][j] == '1': board[i][j] = REPLACE

print(Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])) 

