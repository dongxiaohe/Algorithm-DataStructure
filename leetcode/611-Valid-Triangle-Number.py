class Solution(object):
    def triangleNumber(self, nums):
        count, size = 0, len(nums)
        if size < 3: return count
        nums.sort()
        for c in range(size - 1, 1, -1):
            a, b = 0, c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    count += b - a
                    b -= 1
                else: a += 1
        return count
