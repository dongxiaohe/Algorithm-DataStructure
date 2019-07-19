class Solution:
    def totalHammingDistance(self, nums):
        result = 0
        mask = 1
        size = len(nums)
        for i in range(32):
            count = 0
            for number in nums:
                if number & mask: count += 1
            result += count * (size - count)
            mask <<= 1
        return result

