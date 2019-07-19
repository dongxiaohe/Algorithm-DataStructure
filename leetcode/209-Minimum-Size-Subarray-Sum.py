class Solution:
    def minSubArrayLen(self, s, nums):
        m = len(nums)
        if m == 0: return 0
        start, maxCur, result = 0, 0, float("inf")
        for i in range(len(nums)):
            maxCur += nums[i] 
            while start <= i and maxCur >= s:
                result = min(result, i - start + 1)
                maxCur -= nums[start]
                start += 1
        return result if result != float("inf") else 0
print(Solution().minSubArrayLen(7, [2, 3, 4, 2, 1, 3]))
