class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        result = {}
        for i in range(0, n):
            if target - nums[i] in result:
                return [result[target - nums[i]], i]
            result[nums[i]] = i

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([2, 7, 11, 15, 3], 5))
print(solution.twoSum([2, 7, 11, 15, 30], 37))