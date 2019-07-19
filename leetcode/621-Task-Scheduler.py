class Solution(object):
    def leastInterval(self, tasks, n):
        if n == 0: return len(tasks)
        taskCount = collections.defaultdict(int)
        for task in tasks: taskCount[task] += 1
        pq = []
        for key in taskCount: heapq.heappush(pq, -taskCount[key])
        result, cooling = 0, collections.defaultdict(int)
        while pq or cooling:
            if result - n - 1 in cooling:
                tmpCount = cooling[result - n - 1]
                del cooling[result - n - 1]
                heapq.heappush(pq, tmpCount)
            if pq:
                maxCount = heapq.heappop(pq) + 1
                if maxCount < 0: cooling[result] = maxCount
            result += 1
        return result

