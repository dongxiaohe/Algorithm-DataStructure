class TicTacToe(object):

    def __init__(self, n):
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diagnol = 0
        self.antidiagnol = 0
        self.n = n

    def move(self, row, col, player):
        toAdd = 1 if player == 1 else -1
        self.rows[row] += toAdd
        self.cols[col] += toAdd
        if row == col: self.diagnol += toAdd
        if row + col == self.n - 1: self.antidiagnol += toAdd
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagnol) == self.n or abs(self.antidiagnol) == self.n: return player
        return 0
