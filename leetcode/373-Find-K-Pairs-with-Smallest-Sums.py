class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        pairs = []
        push(0, 0)
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0: push(i + 1, 0)
        return pairs
                
