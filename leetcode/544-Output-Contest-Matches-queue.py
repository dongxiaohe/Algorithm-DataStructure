class Solution(object):
    def findContestMatch(self, n):
        queue = collections.deque()
        for i in range(1, n + 1, 1):
            queue.append(i)
        while n > 2:
            tmp_queue = collections.deque()
            while queue:
                first = queue.popleft()
                last = queue.pop()
                tmp_queue.append((first, last))
            queue = tmp_queue
            n >>= 1
        return str(tuple(queue)).replace(' ', '')

