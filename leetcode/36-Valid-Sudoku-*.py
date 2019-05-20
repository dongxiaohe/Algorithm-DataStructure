class Solution:
    def isValidSudoku(self, board):
        used1 = [[0 for _ in range(9)] for _ in range(9)]
        used2 = [[0 for _ in range(9)] for _ in range(9)]
        used3 = [[0 for _ in range(9)] for _ in range(9)]
        rows = len(board)
        for i in range(rows):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    k = int(i / 3) * 3 + int(j / 3)
                    print(k, num)
                    if used1[i][num] or used2[j][num] or used3[k][num]:
                        print(used2[j][num])    
                        return False
                    used1[i][num], used2[j][num], used3[k][num] = 1, 1, 1
        print(used3)
        return True
valid = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(valid))
