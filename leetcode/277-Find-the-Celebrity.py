class Solution(object):
    def findCelebrity(self, n):
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i): candidate = i
        for i in range(n):
            if candidate != i and (knows(candidate, i) or not knows(i, candidate)): return -1 # bug free
        return candidate
