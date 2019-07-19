class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        def atMostK(nums, k):
            i, count, result = 0, collections.Counter(), 0
            for j in range(len(nums)):
                if count[nums[j]] == 0: k -= 1
                count[nums[j]] += 1
                while k < 0:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0: k += 1
                    i += 1
                result += j - i + 1
            return result
        return atMostK(A, K) - atMostK(A, K - 1)

