class Solution(object):
    def findShortestSubArray(self, nums):
        first, counter, degree, result = {}, collections.defaultdict(int), 0, 0
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            counter[v] += 1
            if counter[v] > degree:
                degree = counter[v]
                result = i - first[v] + 1
            elif counter[v] == degree:
                result = min(result, i - first[v] + 1)
        return result

