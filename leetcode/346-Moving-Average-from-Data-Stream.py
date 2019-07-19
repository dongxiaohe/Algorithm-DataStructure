class MovingAverage(object):

    def __init__(self, size):
        self.arr = collections.deque() # queue + sum
        self.size = size
        self.sum = 0

    def next(self, val):
        if len(self.arr) < self.size:
            self.sum += val
            self.arr.append(val)
            return self.sum / len(self.arr)
        self.sum += -self.arr.popleft() + val
        self.arr.append(val)
        return self.sum  / self.size
