from heapq import *

class MedianFinder(object):
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        minNumber = heappushpop(large, num) # push and pop means refresh
        heappush(small, -minNumber) # push smaller elements into small
        if len(large) < len(small): # gurantee large is always greater or equal to smaller
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return large[0]
        else:
            return (large[0] - small[0]) / 2.0
