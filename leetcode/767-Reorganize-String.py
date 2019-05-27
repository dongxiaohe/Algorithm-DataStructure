class Solution(object):
    def reorganizeString(self, S):
        ch_count = collections.defaultdict(int)
        for ch in S:
            ch_count[ch] -= 1
            if ch_count[ch] < -(len(S) + 1 >> 1): return ""
        heap = []
        for key in ch_count:
            heapq.heappush(heap, [ch_count[key], key])
        result = []
        while len(heap) >= 2:
            count1, ch1 = heapq.heappop(heap)
            count2, ch2 = heapq.heappop(heap)
            result.extend([ch1, ch2])
            if count1 < -1: heapq.heappush(heap, [count1 + 1, ch1])
            if count2 < -1: heapq.heappush(heap, [count2 + 1, ch2])
        if heap: result.append(heap[0][1])
        return "".join(result)

