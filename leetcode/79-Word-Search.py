class Solution:
    def exist(self, board, word):
        def _dfs(board, word, i, j, m, n, wordPosition):
            if len(word) == wordPosition: return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[wordPosition]: return False
            tmp = board[i][j]
            board[i][j] = "*"
            wordPosition += 1
            result = _dfs(board, word, i + 1, j, m, n, wordPosition) or _dfs(board, word, i - 1, j, m, n, wordPosition) or _dfs(board, word, i, j + 1, m, n, wordPosition) or _dfs(board, word, i, j - 1, m, n, wordPosition)
            board[i][j] = tmp
            return result
        if not board: return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if _dfs(board, word, i, j, m, n, 0): return True
        return False
