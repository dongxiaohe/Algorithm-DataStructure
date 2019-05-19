class Solution:
    def threeSum(self, nums):
        return self.threeSumTarget(nums, 0)
    def threeSumTarget(self, nums, target):
        nums.sort()
        l = len(nums)
        result = []
        for i in range(l - 1):
            if i == 0 or nums[i] != nums[i - 1]:
                left = i + 1
                right = l - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if target == total:
                        result.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target: 
                        left += 1
                    else:
                        right -= 1
        return result
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
