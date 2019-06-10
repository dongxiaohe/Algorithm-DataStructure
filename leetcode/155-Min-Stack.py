class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        _min = self.getMin()
        if _min is not None: self.stack.append([x, min(self.getMin(), x)])
        else: self.stack.append([x, x])

    def pop(self):
        if len(self.stack) > 0: return self.stack.pop()[0]

    def top(self):
        if len(self.stack) > 0: return self.stack[-1][0]

    def getMin(self):
        if len(self.stack) == 0: return None
        return self.stack[-1][1]
