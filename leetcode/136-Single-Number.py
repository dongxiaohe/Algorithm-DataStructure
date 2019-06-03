class Solution:
    def singleNumber(self, nums):
        """
        XOR n ^ n = 0 and n ^ 0 = 0, so XOR is commutative
        """
        result = 0
        for i in range(len(nums)):
            result = result ^ nums[i]
        return result
