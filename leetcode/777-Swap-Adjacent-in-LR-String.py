class Solution(object):
    def canTransform(self, start, end):
        if start.replace('X','') != end.replace('X', ''): return False
        for symbol, op in (('L', operator.ge), ('R', operator.le)):
            A = (i for i, ch in enumerate(start) if ch == symbol)
            for i, ch in enumerate(end):
                if ch == symbol and not op(next(A), i): return False
        return True

