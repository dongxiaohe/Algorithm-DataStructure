class Solution(object):
    def __init__(self):
        self.buffer = [""]*4
        self.bufferIndex = 0
        self.bufferCount = 0

    def read(self, buf, n):
        i = 0
        while i < n:
            while i < n and self.bufferIndex < self.bufferCount:
                buf[i] = self.buffer[self.bufferIndex]
                i += 1
                self.bufferIndex += 1
            if i < n:
                self.bufferCount = read4(self.buffer)
                self.bufferIndex = 0
                if self.bufferCount == 0: return i
        return i


