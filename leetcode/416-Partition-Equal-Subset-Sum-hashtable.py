class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total & 1 == 0:
            half = total >> 1
            cur = {0}
            for number in nums:
                cur |= { number + x for x in cur}
                if half in cur: return True
        return False
