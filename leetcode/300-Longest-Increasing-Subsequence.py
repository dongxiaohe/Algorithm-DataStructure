class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) >> 1
                if tails[m] < x: i = m + 1
                else: j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

print(Solution().lengthOfLIS([10,9,2,5,0,3,7,1,101,18]))
