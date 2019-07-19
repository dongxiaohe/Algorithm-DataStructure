class Solution:
    def productExceptSelf(self, nums):
        left, right, size = 1, 1, len(nums)
        result = [1] * size
        for i in range(1, size):
            result[i] = result[i - 1] * nums[i - 1]
        for i in range(size - 1, -1 , -1):    
            result[i] *= right
            right *= nums[i]
        return result
