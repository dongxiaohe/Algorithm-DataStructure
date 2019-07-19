class Solution:
    def topKFrequent(self, nums, k):
        count = collections.defaultdict(int)
        for t in nums:
            count[t] += 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key in count:
            buckets[count[key]].append(key)
        result, i = [], len(nums)
        while k > 0 and i >= 0 :
            if buckets[i]:
                result += buckets[i]
                k -= len(buckets[i])
            i -= 1
        return result    
