class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x[0])
        minHeap = []
        for start, end in intervals:
            if minHeap and start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
        return len(minHeap)
